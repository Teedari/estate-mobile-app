from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.views import APIView
from django.contrib.auth.models import User
# Create your views here.



class CreateUser(ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer
  permission_classes = [permissions.AllowAny,]
  
  
class LoginUser(APIView):
  serializer_class = LoginSerializer
  permission_classes = [permissions.AllowAny,]
  
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    # print(serializer)
    if serializer.is_valid():
      user = serializer.save()
      if user != {}:
        u = LoginSerializer(data=user['user'])
        return Response(
          {'message': 'user logged in', 
           'token': user['token'],
           'data': {
             'username': user['user'].username,
            }
           }, status=status.HTTP_201_CREATED)
    
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)