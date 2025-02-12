from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Doctor, Treatment
from accounts.forms import *

from notifications.models import Notification


# Create your views here.

def docp(request):
    doctor = Doctor.objects.get(user=request.user)
    treatment = Treatment.objects.filter(doctor=doctor)
    return render(request, 'doctors_p/doctorprofile.html', {'doctor': doctor, 'treatments': treatment})


def dnotify(request):
    doctor = Doctor.objects.get(user=request.user)
    my_notifications = Notification.objects.filter(doctor=doctor, accepted=False)
    return render(request, 'doctors_p/dnotify.html', {'doctor': doctor, 'notifications': my_notifications})


def tconfirm(request):
    pk = request.POST.get('pk')
    notification = Notification.objects.get(pk=pk)
    treatment = notification.treatment
    doctor = Doctor.objects.get(user=request.user)
    treatment.doctor = doctor
    notification.accepted = True
    notification.save()
    treatment.save()
    return redirect('doctor:dprof')


def tupdate(request,id):
    if request.method == 'POST':
        treatment = Treatment.objects.get(pk=id)
        form = TreatmentForm1(request.POST,instance=treatment)
        form.save()
        return redirect('doctor:dprof')
    else:
        form = TreatmentForm1()
    return render(request,'doctors_p/addtreat.html',{'form':form,'id':id})

