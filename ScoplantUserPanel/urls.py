from django.urls import path
from .views import *



urlpatterns = [
    path('',add_device, name='add_device'),
    path('device-info/<device_id>/',device_info, name='device_info'),
    path('remove-device/<device_id>',remove_device),
    path('reports/<device_id>', reporting_device, name='reporting'),
    path('get_device_info/<int:device_id>/',get_device_info, name='get_device_info'),
]
