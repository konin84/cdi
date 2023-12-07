from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import UserAccount

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['id'] = user.id
        token['email'] = user.email
        token['role'] = user.role
        token['firstname'] = user.firstname
        token['lastname'] = user.lastname
        token['telephone'] = user.telephone
        token['patient_id'] = user.patient_id
        token['gender'] = user.gender
        # ...

        return token
