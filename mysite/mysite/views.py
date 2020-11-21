from django.http.response import HttpResponse
from django.shortcuts import render,redirect



def home(request):
    return HttpResponse("Hello Users")