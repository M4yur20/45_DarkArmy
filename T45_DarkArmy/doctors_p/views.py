from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *


# Create your views here.

def docp(request):
    doctor = Doctor.objects.get(user=request.user)
    treatment = Treatment.objects.filter(doctor=doctor)
    return render(request, 'doctors_p/doctorprofile.html', {'doctor': doctor, 'treatments': treatment})
