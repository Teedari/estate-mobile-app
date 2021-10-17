from django.urls import path
from .views import NoticeAPI, ComplaintAPI, AllowanceAPI
app_name = 'apis'

urlpatterns = [
  path('complaints', ComplaintAPI.as_view(), name='complaints'),
  path('allowances', AllowanceAPI.as_view(), name='allowances'),
  path('notices', NoticeAPI.as_view(), name='notices'),
]