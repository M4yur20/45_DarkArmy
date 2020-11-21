from django.contrib import admin
from django.urls import path,include
from . import views


app_name='accounts'
urlpatterns=[
    path('patient/signup/',views.psignup,name='psignup'),
    path('doctor/signup/',views.dsignup,name='dsignup'),
    path('iagent/signup/',views.isignup,name='isignup'),
    path('profile/doctor/',views.dprofile,name='dprofile'),
    path('profile/patient/',views.pprofile,name='pprofile'),
    path('profile/agent/',views.aprofile,name='aprofile'),
    path('temp/',views.tp,name='tp'),

]