
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Doctor
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import DoctorForm,PatientForm,AgentForm
from django.contrib.auth.decorators import user_passes_test


def dprofile(request):
    
    if request.method == "POST":
        form=DoctorForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('home')
    else:    
        form=DoctorForm()
    return render(request,'accounts/dprofile.html',{'form':form})

def pprofile(request):
    
    if request.method == "POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            print("Hello")
            return redirect('home')
    else:    
        form=PatientForm()
    return render(request,'accounts/pprofile.html',{'form':form})

def aprofile(request):
    
    if request.method == "POST":
        form=AgentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('home')
    else:    
        form=AgentForm()
    return render(request,'accounts/aprofile.html',{'form':form})


def dsignup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user,is_doctor=True)
            #user_type_signal.send(sender=user,user_type='Student')
            #log the user in
            login(request,user)
            
            return redirect('home')
    else:
       form=UserCreationForm()
    return render(request,'accounts/dsignup.html',{"form":form})



def psignup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user,is_patient=True)
            #user_type_signal.send(sender=user,user_type='Student')
            #log the user in
            login(request,user)
            
            return redirect('home')
    else:
       form=UserCreationForm()
    return render(request,'accounts/psignup.html',{"form":form})


def isignup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user,is_agent=True)
            #user_type_signal.send(sender=user,user_type='Student')
            #log the user in
            login(request,user)
            
            return redirect('home')
    else:
       form=UserCreationForm()
    return render(request,'accounts/isignup.html',{"form":form})



def check_patient(user):
    return user.profile.is_patient

def check_iagent(user):
    return user.profile.is_agent


def check_doctor(user):
    return user.profile.is_doctor


@user_passes_test(check_doctor,login_url='home')
def tp(request):
    return HttpResponse("I am a Doctor")

