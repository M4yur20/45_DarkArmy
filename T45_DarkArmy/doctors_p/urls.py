from django.contrib import admin
from django.urls import path
from . import views
app_name = 'doctor'

urlpatterns = [
    path('doctor/profile', views.docp,name='dprof'),
]