from rest_framework import serializers
from .models import StatProfile

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatProfile
        fields = ('cid','charge_stat')

class GetStatus(serializers.ModelSerializer):
    cid = serializers.CharField(validators=[])

    class Meta:
        model = StatProfile
        fields = ('cid','charge_stat', 'uid')

class CreateStat(serializers.ModelSerializer):
    class Meta:
        model = StatProfile
        fields = ('loc', 'op')