from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .serializers import DoctorSignUpSerializer,  SignUpAdministratorSerializer,  AccountantSignUpSerializer, PatientSignUpSerializer, AccountSerializer,AccountUpdateSerializer, CashierSignUpSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes, APIView
#  importing models
from .models import UserAccount, Cashier, Administrator, Doctor, Accountant,Patient

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from .permissions import IsAdmin, IsRealtor, IsHouseOwner, IsTenant
from rest_framework import generics
#
from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from backend.settings import EMAIL_HOST_USER


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allUsers(request):
    users = UserAccount.objects.all()
    # Converting the Employees query into json
    serializer = AccountSerializer(users, many=True)
    return Response(serializer.data)


# Admins
class SignUpAdministrator(generics.CreateAPIView):
    serializer_class = SignUpAdministratorSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Aministrator Account Creation'
            message = "Dear Admin," + " " + \
                data['firstname'] + " " + data['lastname'] + ". " + \
                "Your account to use this service has been created" + \
                " " + "Your password is: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            print('User Email: ', email)
            print('Company Message: ', message)

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Get all admins
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allAdmins(request):
    admins = Administrator.objects.all()
    serializer = AccountSerializer(admins, many=True)
    return Response(serializer.data)

## Get single admin for update et deletion
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def admin(request, pk):
    try:
        data = Administrator.objects.get(id=pk)
    except Administrator.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountUpdateSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

# Doctors
class SignUpDoctor(generics.CreateAPIView):
    serializer_class = DoctorSignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Doctor Account Creation'
            message = "Dear Doctor," + " " + \
                data['firstname'] + " " + data['lastname'] + ". " + \
                "Your account to use this service has been created" + \
                " " + "Your password is: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            print('User Email: ', email)
            print('Company Message: ', message)

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Get all doctors
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allDoctors(request):
    doctors = Doctor.objects.all()
    serializer = AccountSerializer(doctors, many=True)
    return Response(serializer.data)

## Get single doctor for update et deletion
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def doctor(request, pk):
    try:
        data = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountUpdateSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# Patient Management
class SignUpPatient(generics.CreateAPIView):
    serializer_class = PatientSignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Patient Account Creation'
            message = "Cher(e) Patient(e)," + " " + \
                data['firstname'] + " " + data['lastname'] + ". " + \
                "Votre compte a été créé avec success" + \
                " " + "Votre mot de passe est: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            print('User Email: ', email)
            print('Company Message: ', message)

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Get all patients
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allPatients(request):
    patients = Patient.objects.all()
    serializer = AccountSerializer(patients, many=True)
    return Response(serializer.data)

## Get single patient for update et deletion
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def patient(request, pk):
    try:
        data = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountUpdateSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cashier Management
class SignUpCashier(generics.CreateAPIView):
    serializer_class = CashierSignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Creation du Réceptionniste '
            message = "Cher(e) Réceptionniste ," + " " + \
                data['firstname'] + " " + data['lastname'] + ". " + \
                "Votre compte a été créé avec success" + \
                " " + "Votre mot de passe est: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            print('User Email: ', email)
            print('Company Message: ', message)

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Get all patients
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allCashiers(request):
    cashiers = Cashier.objects.all()
    serializer = AccountSerializer(cashiers, many=True)
    return Response(serializer.data)

## Get single patient for update et deletion
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def cashier(request, pk):
    try:
        data = Cashier.objects.get(id=pk)
    except Cashier.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountUpdateSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cashier Management
class SignUpAccountant(generics.CreateAPIView):
    serializer_class = AccountantSignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Creation de Comptable '
            message = "Cher(e) Comptable ," + " " + \
                data['firstname'] + " " + data['lastname'] + ". " + \
                "Votre compte a été créé avec success" + \
                " " + "Votre mot de passe est: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            print('User Email: ', email)
            print(' Message: ', message)

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Get all patients
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allAccountants(request):
    accountants = Accountant.objects.all()
    serializer = AccountSerializer(accountants, many=True)
    return Response(serializer.data)

## Get single patient for update et deletion
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def accountant(request, pk):
    try:
        data = Accountant.objects.get(id=pk)
    except Accountant.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountUpdateSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

