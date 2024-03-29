from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import Wallet

class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.IntegerField(
            validators=[UniqueValidator(queryset=User.objects.all())],
            required = True,
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        wallet = Wallet.objects.create(
            uid=self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        wallet.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        # firstname = user.first_name
        # lastname = user.lastname
        print(type(token))
        return token
    


class UpdateWalletwid(serializers.ModelSerializer):
    wid = serializers.CharField(validators=[])

    class Meta:
        model = Wallet
        fields = ('wid', 'amount')

class UpdateWalletuid(serializers.ModelSerializer):
    uid = serializers.IntegerField(validators=[])

    class Meta:
        model = Wallet
        fields = ('uid', 'amount')

class UpdateWalletwid(serializers.ModelSerializer):
    wid = serializers.CharField(validators=[])

    class Meta:
        model = Wallet
        fields = ('wid', 'amount')

class UpdateWalletuid(serializers.ModelSerializer):
    uid = serializers.IntegerField(validators=[])

    class Meta:
        model = Wallet
        fields = ('uid', 'amount',)
        extra_kwargs = {
            'uid': {'required': False},
            'amount': {'required': False}
        }


class GetWalletwid(serializers.ModelSerializer):
    wid = serializers.CharField(validators=[])

    class Meta:
        model = Wallet
        fields = '__all__'

class GetWalletuid(serializers.ModelSerializer):
    uid = serializers.IntegerField(validators=[])

    class Meta:
        model = Wallet
        fields = '__all__'

class GetName(serializers.ModelSerializer):
    uid = serializers.IntegerField(validators=[])

    class Meta:
        model = Wallet
        fields = ('uid', 'first_name', 'last_name',)