from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name='noti'

urlpatterns = [
    path('noti/', views.noti, name='noti'),
    ]