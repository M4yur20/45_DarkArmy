from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *


# Create your views here.

def agp(request):
    agent=Agent.objects.get(user=request.user)
    return render(request,'agents_p/agentprof.html',{'agent':agent})
