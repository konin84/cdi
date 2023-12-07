from rest_framework import serializers
from rest_framework.validators import ValidationError
# 
from .models import UserAccount, Patient, Administrator, Cashier, Doctor, Accountant


class SignUpAdministratorSerializer(serializers.ModelSerializer):
  
  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  firstname = serializers.CharField(max_length=20)
  lastname = serializers.CharField(max_length=50)
  telephone = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)

  class Meta:
    model = Administrator
    fields = ['id', 'email',  'password', 'firstname', 'lastname', 'telephone', 'gender']


  def validate(self, attrs):
    email_exists = Administrator.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Administrator.objects.create(
                  email=validated_data['email'],
                  firstname = validated_data['firstname'],
                  lastname = validated_data['lastname'],
                  telephone = validated_data['telephone'],
                  gender = validated_data['gender'],
                    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class DoctorSignUpSerializer(serializers.ModelSerializer):

  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  firstname = serializers.CharField(max_length=20)
  lastname = serializers.CharField(max_length=50)
  telephone = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)

  class Meta:
    model = Doctor
    fields = '__all__'
    fields = ['id', 'email',  'password', 'firstname', 'lastname', 'telephone', 'gender']

  def validate(self, attrs):
    email_exists = Doctor.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Doctor.objects.create(
                  email=validated_data['email'],
                  firstname = validated_data['firstname'],
                  lastname = validated_data['lastname'],
                  telephone = validated_data['telephone'],
                  gender = validated_data['gender'],
    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
        extra_kwargs = {
           'password':{
              'write_only':True
           }
        }

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email',  'firstname', 'lastname', 'telephone', 'gender']


class AccountInfoForMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email',  'firstname', 'lastname', 'telephone']
  

class AccountantSignUpSerializer(serializers.ModelSerializer):

  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  firstname = serializers.CharField(max_length=20)
  lastname = serializers.CharField(max_length=50)
  telephone = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)

  class Meta:
    model = Accountant
    fields = '__all__'
    fields = ['id', 'email',  'password', 'firstname', 'lastname', 'telephone', 'gender']

  def validate(self, attrs):
    email_exists = Accountant.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Accountant.objects.create(
                  email=validated_data['email'],
                  firstname = validated_data['firstname'],
                  lastname = validated_data['lastname'],
                  telephone = validated_data['telephone'],
                  gender = validated_data['gender'],
    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class CashierSignUpSerializer(serializers.ModelSerializer):

  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  firstname = serializers.CharField(max_length=20)
  lastname = serializers.CharField(max_length=50)
  telephone = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)

  class Meta:
    model = Cashier
    fields = '__all__'
    fields = ['id', 'email',  'password', 'firstname', 'lastname', 'telephone', 'gender']

  def validate(self, attrs):
    email_exists = Cashier.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Cashier.objects.create(
                  email=validated_data['email'],
                  firstname = validated_data['firstname'],
                  lastname = validated_data['lastname'],
                  telephone = validated_data['telephone'],
                  gender = validated_data['gender'],
    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class PatientSignUpSerializer(serializers.ModelSerializer):

  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  firstname = serializers.CharField(max_length=20)
  lastname = serializers.CharField(max_length=50)
  telephone = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)
  patient_id = serializers.IntegerField()

  class Meta:
    model = Patient
    fields = '__all__'
    fields = ['id', 'email',  'password', 'firstname', 'lastname', 'telephone', 'gender', 'patient_id']

  def validate(self, attrs):
    email_exists = Patient.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Patient.objects.create(
                  email=validated_data['email'],
                  firstname = validated_data['firstname'],
                  lastname = validated_data['lastname'],
                  telephone = validated_data['telephone'],
                  gender = validated_data['gender'],
                  patient_id = validated_data['patient_id'],
    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class FirstnameLastnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','firstname', 'lastname','patient_id',]

