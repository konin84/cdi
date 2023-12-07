from .serializers import ClinicInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import ClinicInfo


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ClinicInfoData(request):
    if request.method == 'GET':
        data = ClinicInfo.objects.all()
        serializer = ClinicInfoSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialiazer = ClinicInfoSerializer(data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'Adding new ClinicInfo': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def ClinicInfoSetting(request, pk):
    try:
        data = ClinicInfo.objects.get(id=pk)
    except ClinicInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiazer = ClinicInfoSerializer(data)
        return Response(serialiazer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialiazer = ClinicInfoSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def PublicClinicData(request):
    if request.method == 'GET':
        data = ClinicInfo.objects.all()
        serializer = ClinicInfoSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

