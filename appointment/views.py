from .serializers import AppointmentSerializer,UpdateAppointmentSerializer,AppointmentInfoSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Appointment

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def AppointmentData( request):

  if request.method=='GET':   
     data=Appointment.objects.all() 
     serializer = AppointmentInfoSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = AppointmentSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'Setting new Appointment':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def AppointmentSetting (request, pk):
   try:
      data = Appointment.objects.get(id=pk)
   except Appointment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = AppointmentInfoSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = UpdateAppointmentSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Appointment': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
   

