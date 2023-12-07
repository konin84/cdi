from .serializers import TreatmentSerializer, InterventionSerializer,TreatmentUpdateStausSerializer,TreatmentInfoSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Treatment, Intervention
# Create your views here.



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def InterventionData( request):

  if request.method=='GET':   
     data=Intervention.objects.all() 
     serializer = InterventionSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = InterventionSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'Adding new Intervention':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def PublicInterventionData( request):

  if request.method=='GET':   
     data=Intervention.objects.all() 
     serializer = InterventionSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def TreatmentData( request):

  if request.method=='GET':   
     data=Treatment.objects.all() 
     serializer = TreatmentInfoSerializer(data, many=True)

     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = TreatmentSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response(serialiazer.data, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def InterventionSetting (request, pk):
   try:
      data = Intervention.objects.get(name=pk)
   except Intervention.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = InterventionSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   elif request.method == 'PUT':
      serialiazer = InterventionSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Intervention': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def TreatmentSetting (request, pk):
   try:
      data = Treatment.objects.get(id=pk)
   except Treatment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = TreatmentInfoSerializer(data)
      return Response(serialiazer.data, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = TreatmentSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Treatment': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
   

@api_view(['PUT'])
def UpdateTreatmentStatus(request, pk): 
      try:
         data = Treatment.objects.get(id=pk)
      except Treatment.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
      if request.method=='PUT':   
         data.treatmentstatus="Terminé"
         serialiazer = TreatmentUpdateStausSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Treatment': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
   


@api_view(['PUT'])
def UpdateTreatmentPaymentStatus(request, pk): 
      try:
         data = Treatment.objects.get(id=pk)
      except Treatment.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
      if request.method=='PUT':   
         data.statuspayment="Payé"
         serialiazer = TreatmentUpdateStausSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Treatment': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
   


