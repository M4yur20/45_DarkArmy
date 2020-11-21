from django.contrib import admin
from django.urls import path
from . import views
app_name = 'pp'

urlpatterns = [
    path('patient/profile/',views.patprof,name='patprof'),
]