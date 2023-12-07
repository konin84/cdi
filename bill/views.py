from .serializers import PaymentSerializer,PaymentInfoSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Payment

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def PaymentData( request):

  if request.method=='GET':   
     data=Payment.objects.all() 
     serializer = PaymentInfoSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    serialiazer = PaymentSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'Setting new Payment':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def PatientSetting (request, pk):
   try:
      data = Payment.objects.get(id=pk)
   except Payment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = PaymentSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK) 
   elif request.method == 'PUT':
      serialiazer = PaymentSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Payment': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
