from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import *


def home(request):
    loh = Hospital.objects.all()
    loa = Agent.objects.all()
    return render(request, 'home.html', {'loh': loh,'loa':loa})


'''
{% for i in loh %}
    <strong> i.name </strong>
{% endfor %}

{% for j in loa %}
    <strong> j.first_name j.last_name </strong>
{% endfor %}


Doctors own Treatment History
doctor = Doctor.objects.get(user=request.user)
mytreatment = Treatment.objects.filter(doctor=doctor)
{'treatments':mytreatment}

In html file

{% for treat in treatments %}
    {{treat.patient}}
    {{treat.hospital}}
    {{treat.injury_type}}
    {{treat.injury_description}}
    <br>
{%endfor%}


Patients own Treatment History
patient=Patient.objects.get(user=request.user)
mytreatments=Treatment.objects.filter(patient=patient)
{'treatments':mytreatment}

In Html file

{% for treat in treatments %}
    {{treat.doctor}}
    {{treat.hospital}}
    {{treat.injury_type}}
    {{treat.injury_description}}
    <br>
{%endfor%}

'''
