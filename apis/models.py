from django.db import models

# Create your models here.


class Notice(models.Model):
  applicant = models.CharField(max_length=100)
  contact = models.CharField(max_length=10,)
  facility = models.CharField(max_length=100)
  comment = models.TextField(blank=True)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  
class Complaint(models.Model):
  name = models.CharField(max_length=100)
  contact = models.CharField(max_length=10)
  building = models.CharField(max_length=100)
  complaint_type = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  comment = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
class Allowance(models.Model):
  name = models.CharField(max_length=200)
  introduction = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  address = models.CharField(max_length=200)
  floor_area = models.CharField(max_length=100)
  distance = models.FloatField()
  rent_per_month = models.PositiveIntegerField()
  rent_per_annum = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)