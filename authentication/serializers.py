from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, models
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
  
  class Meta:
    model =  User
    fields = ('username', 'email', 'password',)
    
    
    
  def create(self, validated_data):
    instance = validated_data
    user = User.objects.create(username=instance.get('username'))
    user.email = instance.get('email')
    user.set_password(instance.get('password'))
    user.save()
    return user
  
  
  
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(required=True, max_length=100)
  password = serializers.CharField(required=True, max_length=100)
  
  def create(self, validated_data):
    user = authenticate(username=validated_data.get('username'), password=validated_data.get('password'))
    token = None
    if user is not None:
      
      if Token.objects.filter(user = user).exists():
        token = Token.objects.filter(user = user)[0]
      else:
        token = Token.objects.create(user=user)
        token.save()
      return {
        'user': user,
        'token': token.key,
      }
    # else: 
    #   raise exceptions.ValidationError('Invalid credentials')
    return {}
        
  
  
  