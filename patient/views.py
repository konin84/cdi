from .serializers import PatientSerializer, PatientMessageSerializer, PatientMessageInfoSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Patient, PatientMessage
# Create your views here.


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def PatientData( request):

  if request.method=='GET':   
     data=Patient.objects.all() 
     serializer = PatientSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = PatientSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'Adding new Patient':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def PatientSetting (request, pk):
   try:
      data = Patient.objects.get(id=pk)
   except Patient.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = PatientSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = PatientSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Patient': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def MessageData( request):

  if request.method=='GET':   
     data=PatientMessage.objects.all() 
     serializer = PatientMessageInfoSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = PatientMessageSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response(serialiazer.data, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def MessageSetting (request, pk):
   try:
      data = PatientMessage.objects.get(id=pk)
   except PatientMessage.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = PatientMessageInfoSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = PatientMessageSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response(serialiazer.data, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def messageInfo(request):
#     if request.method == 'GET':
#         data = ClinicInfo.objects.all()
#         serializer = ClinicInfoSerializer(data, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

