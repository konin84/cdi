from django.shortcuts import render
from .serializers import ExpenseTypeSerializer, ExpenseSerializer, ExpenseInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Expense, ExpenseTypes

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated, IsAdminUser])
def ExpenseTypeData(request):
    if request.method == 'GET':
        data = ExpenseTypes.objects.all()
        serializer = ExpenseTypeSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialiazer = ExpenseTypeSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ExpenseTypeSetting(request, pk):
    try:
        data = ExpenseTypes.objects.get(id=pk)
    except ExpenseTypes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = ExpenseTypeSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = ExpenseTypeSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def ExpenseData(request):
    if request.method == 'GET':
        data = Expense.objects.all()
        serializer = ExpenseInfoSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialiazer = ExpenseSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response( serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def ExpenseSetting(request, pk):

    try:
        data = Expense.objects.get(id=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = ExpenseSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = ExpenseSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
    
