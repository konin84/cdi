from django.shortcuts import render
from .serializers import InsuranceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
#  importing models
from .models import Insurance
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def insuranceData(request):

    if request.method == 'GET':
        data = Insurance.objects.all()
        serializer = InsuranceSerializer(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialiazer = InsuranceSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Adding new insurance': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def PublicInsuranceData(request):

    if request.method == 'GET':
        data = Insurance.objects.all()
        serializer = InsuranceSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def InsuranceSetting(request, pk):
    try:
        data = Insurance.objects.get(insurancename=pk)
    except Insurance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = InsuranceSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = InsuranceSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Insurance': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
