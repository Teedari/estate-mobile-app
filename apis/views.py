from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from .models import *

from apis.serializers import AllowanceSerializer, ComplaintSerializer, NoticeSerializer



class NoticeAPI(ListCreateAPIView):
  serializer_class = NoticeSerializer
  permission_classes = [permissions.AllowAny,]
  queryset = Notice.objects.all()
  
class ComplaintAPI(ListCreateAPIView):
  serializer_class = ComplaintSerializer
  permission_classes = [permissions.AllowAny,]
  queryset = Complaint.objects.all()
  
class AllowanceAPI(ListCreateAPIView):
  serializer_class = AllowanceSerializer
  permission_classes = [permissions.AllowAny,]
  queryset = Allowance.objects.all()
  
  