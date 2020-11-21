from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from tensorflow.python.keras.saving.save import load_model
from .models import Profile, Doctor
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom
from django.contrib.auth.decorators import user_passes_test

'''import cv2
import numpy as np
from keras.models import model_from_json
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam

labels = ['Bite', 'Burns', 'Cuts', 'Fractures']

'''
def nearesthosps(request):
    geolocator = Nominatim(user_agent='accounts')
    if request.method == "POST":
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            patient = Patient.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.patient = patient
            instance.save()
            img = cv2.imread(instance.image.path)
            json_file = open(r'C:\Users\mishr\Downloads\model3.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            loaded_model.load_weights(r'C:\Users\mishr\Downloads\model3.h5')
            loaded_model.compile(loss=categorical_crossentropy,
                                 optimizer=Adam(lr=0.001),
                                 metrics=['accuracy'])
            img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_AREA)
            img = np.array(img, 'float32')
            preds = loaded_model.predict(img.reshape(-1, 300, 300, 3))
            output = labels[np.argmax(preds)]

            location_ = patient.address
            location = geolocator.geocode(location_)
            # location coordinates
            l_lat = location.latitude
            l_lon = location.longitude
            pointA = (l_lat, l_lon)

            des = Hospital.objects.all()
            dic = []
            for dest in des:
                destination = geolocator.geocode(dest.address)
                # destination co-ordinates
                d_lat = destination.latitude
                d_lon = destination.longitude
                pointB = (d_lat, d_lon)
                distance = round(geodesic(pointA, pointB).km, 2)

                dic.append([dest, distance])
            dic.sort(key=lambda item: item[1])
            nearest = dic[0][0]

            return render(request, 'accounts/suggestions.html', {'output': output,
                                                                 'hospital': nearest})
    else:
        form = TreatmentForm()
    return render(request, 'accounts/addimg.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def hosp_reg(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            doctor = Doctor.objects.get(user=request.user)
            instance = form.save()
            instance.doctor.add(doctor)
            return redirect('home')
    else:
        form = HospitalForm()
    return render(request, 'accounts/hospreg.html', {'form': form})


def dprofile(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('doctor:dprof')
    else:
        form = DoctorForm()
    return render(request, 'accounts/dprofile.html', {'form': form})


def pprofile(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('pp:patprof')
    else:
        form = PatientForm()
    return render(request, 'accounts/pprofile.html', {'form': form})


def aprofile(request):
    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('agp:agtp')
    else:
        form = AgentForm()
    return render(request, 'accounts/aprofile.html', {'form': form})


def dsignup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, is_doctor=True)
            # user_type_signal.send(sender=user,user_type='Student')
            # log the user in
            login(request, user)
            return redirect('accounts:dprofile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/dsignup.html', {"form": form})


def psignup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, is_patient=True)
            # user_type_signal.send(sender=user,user_type='Student')
            # log the user in
            login(request, user)
            return redirect('accounts:pprofile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/psignup.html', {"form": form})


def isignup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, is_agent=True)
            # user_type_signal.send(sender=user,user_type='Student')
            # log the user in
            login(request, user)
            return redirect('accounts:aprofile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/isignup.html', {"form": form})


def ilogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('agp:agtp')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/ilogin.html', {'form': form})


def plogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('pp:patprof')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/plogin.html', {'form': form})


def dlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('doctor:dprof')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/dlogin.html', {'form': form})


def check_patient(user):
    return user.profile.is_patient


def check_iagent(user):
    return user.profile.is_agent


def check_doctor(user):
    return user.profile.is_doctor


@user_passes_test(check_doctor, login_url='home')
def tp(request):
    return HttpResponse("I am a Doctor")
