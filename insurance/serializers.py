from rest_framework import serializers

from .models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class InsurancenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['insurancename', 'id']
