from rest_framework.response import Response
from rest_framework import generics,status
from .models import StatProfile
from .serializers import ViewSerializer, GetStatus, CreateStat
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from time import sleep


class ProfileView(generics.ListAPIView):
    queryset = StatProfile.objects.all()
    serializer_class = ViewSerializer

class PollStat(APIView):
    serializer_class = GetStatus
    lookup_url_kwarg = 'cid'

    def get(self, request, format=None):
        cid = request.GET.get(self.lookup_url_kwarg)
        print(cid)
        if cid != None:
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

class CreateStat(APIView):

    serializer_class = CreateStat

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            op = serializer.data.get('op')
            loc = serializer.data.get('loc')

            stat = StatProfile.objects.create(
                op=op,
                loc=loc
            )
            stat.save()

            code = stat.cid

            return Response({'msg':'Station profile is created', 'cid':code, 'created_at':stat.created_at}, status=status.HTTP_200_OK)
        return Response({'msg': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)