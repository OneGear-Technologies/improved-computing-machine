from django.contrib.auth.models import User
from .models import Wallet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    UpdateWalletwid,
    UpdateWalletuid,
    GetWalletuid,
    GetWalletwid,
    GetName
)
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
import json


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
            return Response(UpdateWalletuid(wallet).data, status=status.HTTP_200_OK)
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        return Response({'msg': 'this is a get request'}, status=status.HTTP_408_REQUEST_TIMEOUT)


class Getwid(APIView):
    serializer_class = GetWalletwid
    lookup_url_kwarg = 'wid'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            wid = serializer.data.get('wid')
            queryset = Wallet.objects.get(wid=wid)

            try:
                return Response(GetWalletwid(queryset).data, status=status.HTTP_200_OK)
            except Exception as e:
                if queryset.DoesNotExist:
                    return Response({'msg': 'wallet doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        wid = request.GET.get(self.lookup_url_kwarg)
        if wid != None:
            try:
                queryset = Wallet.objects.get(wid=wid)
            except Wallet.DoesNotExist:
                    return Response({'msg': 'wallet doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response(GetWalletwid(queryset).data, status=status.HTTP_200_OK)
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)  


class Getuid(APIView):
    serializer_class = GetWalletuid
    lookup_url_kwarg = 'uid'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = serializer.data.get('uid')
            queryset = Wallet.objects.get(uid=uid)
            
            try:
                queryset = Wallet.objects.get(uid=uid)
            except Wallet.DoesNotExist:
                return Response({'msg':'uid does not exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response(GetWalletuid(queryset).data, status=status.HTTP_200_OK)
        
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        uid = request.GET.get(self.lookup_url_kwarg)
        if uid != None:
            try:
                queryset = Wallet.objects.get(uid=uid)
            except Wallet.DoesNotExist:
                    return Response({'msg': 'user doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response(GetWalletuid(queryset).data, status=status.HTTP_200_OK)
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)  




class GetNameView(APIView):
    serializer_class = GetName
    lookup_url_kwarg = 'uid'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = serializer.data.get('uid')
            queryset = Wallet.objects.get(uid=uid)
            
            if not queryset.DoesNotExist():
                return Response({'msg': 'user doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response(GetName(queryset).data, status=status.HTTP_200_OK)
        
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        uid = request.GET.get(self.lookup_url_kwarg)
        if uid != None:
            try:
                queryset = Wallet.objects.get(uid=uid)
                first_name=GetWalletuid(queryset).data['first_name']
                last_name=GetWalletuid(queryset).data['last_name']
            except Wallet.DoesNotExist:
                    return Response({'msg': 'user doesnot exists'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'first_name':first_name, 'last_name':last_name}, status=status.HTTP_200_OK)
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)  
