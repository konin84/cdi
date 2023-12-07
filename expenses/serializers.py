from rest_framework import serializers
from .models import Expense, ExpenseTypes



class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTypes
        fields = '__all__'

class ExpenseTypeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTypes
        fields = ['id', 'name']



class ExpenseSerializer(serializers.ModelSerializer):
    # expense = ExpenseTypeInfoSerializer()
    class Meta:
        model = Expense
        fields = '__all__'



class ExpenseInfoSerializer(serializers.ModelSerializer):
    expense = ExpenseTypeInfoSerializer()
    class Meta:
        model = Expense
        fields = '__all__'

