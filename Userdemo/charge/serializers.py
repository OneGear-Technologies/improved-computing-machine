from rest_framework import serializers
from .models import StatProfile

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatProfile
        fields = ('cid','charge_stat')

class GetStatus(serializers.ModelSerializer):
    cid = serializers.IntegerField(validators=[])
    uid = serializers.IntegerField(validators=[])

    class Meta:
        model = StatProfile
        fields = ('cid','charge_stat', 'uid')




