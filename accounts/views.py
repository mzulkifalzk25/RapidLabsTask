from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import UserProfile
from .serializers import UserProfileSerializer, CustomTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User Created Successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    data = []
    if serializer.is_valid():
        data.append(serializer.validated_data)
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
