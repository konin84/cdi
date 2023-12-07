
from .models import Appointment
from account.serializers import FirstnameLastnameSerializer
from patient.serializers import PatientLimitedInfoSerializer

from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    # patient = PatientLimitedInfoSerializer()
    # user = FirstnameLastnameSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'
        # exclude = ('patient','user',)


class AppointmentInfoSerializer(serializers.ModelSerializer):
    patient = PatientLimitedInfoSerializer()
    user = FirstnameLastnameSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'
        # exclude = ('patient','user',)


class UpdateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        # fields = '__all__'
        exclude = ('patient','user',)