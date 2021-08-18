from django.contrib.auth import authenticate
from authentication.models import MyUser
from authentication.serializers import UserLoginSerializer, UserRegisterSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request,format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request,format=None):
        print(request.body)
        email=request.data.get('email',None)
        password=request.data.get('password',None)
        user = authenticate(username=email,password=password)
        if user:
            serializer = UserLoginSerializer(user)
            # if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'no such email'}, status=status.HTTP_400_BAD_REQUEST)