from rest_framework import serializers
from .models import ClinicInfo


class ClinicInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicInfo
        fields = '__all__'


class ClinicUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicInfo
        fields = ['id', 'name']



