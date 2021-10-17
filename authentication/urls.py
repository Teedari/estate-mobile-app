from django.urls import path
from .views import CreateUser, LoginUser


# app_name='authentication'

urlpatterns = [
  path('user/create', CreateUser.as_view(), name='registration'),
  path('user/login', LoginUser.as_view(), name='login')
]