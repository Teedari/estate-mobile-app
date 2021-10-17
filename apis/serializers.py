from rest_framework import serializers

from apis.models import Allowance, Complaint, Notice

class NoticeSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Notice
    fields = '__all__'
    ordering = ('-created_at')
    
    
class ComplaintSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Complaint
    fields = '__all__'
    ordering = ('-created_at')
    
class AllowanceSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Allowance
    fields = '__all__'
    ordering = ('-created_at')