from rest_framework import serializers
from .models import Wallet

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('wid','amount')


class UpdateWalletSerializer(serializers.ModelSerializer):
    wid = serializers.CharField(validators=[])

    class Meta:
        model = Wallet
        fields = ('wid', 'amount')