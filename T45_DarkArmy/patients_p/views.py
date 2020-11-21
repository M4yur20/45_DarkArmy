from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def patprof(request):

    return render(request,'patient_p/patientp.html')
