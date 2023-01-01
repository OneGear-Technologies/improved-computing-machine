from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import WalletSerializer, UpdateWalletSerializer, ViewSerializer
from .models import Wallet
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class WalletView(generics.ListAPIView):
    queryset=Wallet.objects.all()
    serializer_class = ViewSerializer

class CreateWallet(LoginRequiredMixin, APIView):
    serializer_class = WalletSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = get_object_or_404(User, username=request.user.username)
            wid = serializer.data.get('wid')
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(wid=wid)
            if queryset.exists():
                wallet = queryset[0]
                wallet.uid = uid
                wallet.wid = wid
                wallet.amount = amount
                wallet.save(update_fields = ['uid', 'wid','amount'])
                return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)

            else:
                wallet = Wallet(uid=uid, wid=wid, amount=amount)
                wallet.save()
                return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)


class UpdateWallet(APIView, LoginRequiredMixin):
    serializer_class = UpdateWalletSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uid = get_object_or_404(User, username=request.user.username)
            wid = serializer.data.get('wid')
            amount = serializer.data.get('amount')
            queryset = Wallet.objects.filter(wid=wid)
            
            if not queryset.exists():
                return Response({'msg': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)

            wallet=queryset[0]
            if wallet.uid != uid:
                return Response({'msg': 'Unauthorised Access.'}, status=status.HTTP_401_UNAUTHORIZED)
            
            wallet.amount = wallet.amount + amount
            wallet.save(update_fields=['amount'])
            return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)
        
        return Response({'msg':'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)