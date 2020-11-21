from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *


# Create your views here.

def patprof(request):
    patient=Patient.objects.get(user=request.user)
    mytreatments = Treatment.objects.filter(patient=patient)
    return render(request,'patients_p/patientp.html',{'patient':patient,'mytreats':mytreatments})
