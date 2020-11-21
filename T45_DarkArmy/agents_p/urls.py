from django.contrib import admin
from django.urls import path
from . import views
app_name = 'agp'

urlpatterns = [
    path('agent/profile/',views.agp,name='agtp'),
]