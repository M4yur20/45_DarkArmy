from django.contrib import admin
from django.urls import path,include
from . import views

app_name='accounts'

urlpatterns=[
    path('patient/signup/',views.psignup,name='psignup'),
    path('doctor/signup/',views.dsignup,name='dsignup'),
    path('iagent/signup/',views.isignup,name='isignup'),
    path('patient/login/', views.plogin, name='plogin'),
    path('doctor/login/', views.dlogin, name='dlogin'),
    path('iagent/login/', views.ilogin, name='ilogin'),
    path('profile/doctor/',views.dprofile,name='dprofile'),
    path('profile/patient/',views.pprofile,name='pprofile'),
    path('profile/agent/',views.aprofile,name='aprofile'),
    path('hospital/register/',views.hosp_reg,name='hreg'),
    path('nearesthosps/',views.nearesthosps,name='nhosps'),
    path('logout/', views.logout_view, name='logout'),
    path('temp/',views.tp,name='tp'),

]