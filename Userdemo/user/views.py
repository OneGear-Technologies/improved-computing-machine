from django.contrib.auth.models import User
from .models import Wallet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    UpdateWalletwid,
    UpdateWalletuid
)
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class Updatewid(APIView):
    serializer_class = UpdateWalletwid

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            wid = serializer.data.get('wid')
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(wid=wid)
            
            if not queryset.exists():
                return Response({'msg': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)

            wallet=queryset[0]

            wallet.amount = wallet.amount + amount
            wallet.save(update_fields=['amount'])
            return Response(UpdateWalletwid(wallet).data, status=status.HTTP_200_OK)
        
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)



class Updateuid(APIView):
    serializer_class = UpdateWalletuid

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = serializer.data.get('uid')
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(uid=uid)
            
            if not queryset.exists():
                return Response({'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            wallet=queryset[0]

            wallet.amount = wallet.amount + amount
            wallet.save(update_fields=['amount'])
            return Response(UpdateWalletwid(wallet).data, status=status.HTTP_200_OK)
        
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)