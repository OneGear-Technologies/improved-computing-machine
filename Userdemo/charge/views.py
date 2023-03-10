from rest_framework.response import Response
from rest_framework import generics,status
from .models import StatProfile
from .serializers import ViewSerializer, GetStatus
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from time import sleep


class ProfileView(generics.ListAPIView):
    queryset = StatProfile.objects.all()
    serializer_class = ViewSerializer

class PollStat(APIView):
    serializer_class = GetStatus

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cid = serializer.data.get('cid')
            try:
                queryset = StatProfile.objects.get(cid=cid)
            except StatProfile.DoesNotExist:
                return Response({'msg':'cid does not exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response(GetStatus(queryset).data, status=status.HTTP_200_OK)
        
        return Response({'msg': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)


class LockStat(APIView):
    serializer_class = GetStatus
    lookup_url_kwarg = 'cid'
    def unlock(self, stat,cid):
        stat.user = None
        stat.charge_stat = False
        stat.save(update_fields=['uid','charge_stat'])
        print(f'{cid} is available')

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cid = serializer.data.get('cid')
            uid = serializer.data.get('uid')
            user = get_object_or_404(User, username=uid)
            queryset = StatProfile.objects.filter(cid=cid)
            if not queryset.exists():
                return Response({'msg':'cid does not exists'}, status=status.HTTP_404_NOT_FOUND)
            
            stat = queryset[0]
            stat.user = user
            if stat.charge_stat == True:
                return Response({'msg': 'The cid is already active'}, status=status.HTTP_400_BAD_REQUEST)


            stat.charge_stat = True
            stat.save(update_fields=['uid','charge_stat'])
            print(f"{cid} is being aquired")
            sleep(1*60)
            self.unlock(stat,cid)
            return Response(GetStatus(stat).data, status=status.HTTP_200_OK)
        
        return Response({'msg': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)



