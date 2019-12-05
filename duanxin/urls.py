
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'duanxin'
urlpatterns = [
    path('', views.index),
    path('redis/',views.test_redis,name="redis"),
    path('send_sms/',views.send_sms,name="send_sms"),
    path('check_sms/',views.check_sms,name="check_sms"),
]

