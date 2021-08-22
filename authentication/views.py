from django.contrib.auth.models import AnonymousUser
from authentication.customAuthentication import MyAuthentication, MyCustomAuthentication, MyCustomPermission
from django.utils import timezone
from django.contrib.auth import authenticate
from authentication.models import MyUser
from authentication.serializers import UserLoginSerializer, UserRegisterSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getUserDetail(self, request, format=None):
#     serializer=UserRegisterSerializer(request.user)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([])
# def register(self, request,format=None):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserRegisterView(APIView):
#     authentication_classes = []
#     def post(self, request,format=None):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def getUserDetail(self, request, format=None):
#         serializer=UserRegisterSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    authentication_classes = [MyCustomAuthentication]
    permission_classes=[MyCustomPermission]
    # @action(detail=True, methods=['post'], authentication_classes = [], permission_classes=[])
    def post(self, request,format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['get'], authentication_classes = [MyAuthentication], permission_classes=[IsAuthenticated])
    def get(self, request, format=None):
        serializer=UserRegisterSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserLoginView(APIView):
    authentication_classes = []

    def post(self, request,format=None):
        email=request.data.get('email',None)
        password=request.data.get('password',None)
        user = authenticate(username=email,password=password)
        if user:
            # if serializer.is_valid():
            if not user.is_superuser:
                user.last_login=timezone.now()
                user.save()
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'no such email'}, status=status.HTTP_400_BAD_REQUEST)

