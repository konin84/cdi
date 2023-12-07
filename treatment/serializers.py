from rest_framework import serializers

from .models import Treatment, Intervention
from account.serializers import FirstnameLastnameSerializer
from patient.serializers import PatientLimitedInfoSerializer


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'
        
class TreatmentInfoSerializer(serializers.ModelSerializer):
    user = FirstnameLastnameSerializer()
    patient = PatientLimitedInfoSerializer()
    class Meta:
        model = Treatment
        fields = '__all__'


class TreatmentUpdateStausSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['id']
