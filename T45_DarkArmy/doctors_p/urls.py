from django.contrib import admin
from django.urls import path
from . import views
app_name = 'doctor'

urlpatterns = [
    path('doctor/profile', views.docp,name='dprof'),
    path('doctor/notifications',views.dnotify,name='dnotify'),
    path('treatment/confirm',views.tconfirm,name='tconfirm'),
    path('treatment/<int:id>/',views.tupdate,name='tupdate')
]