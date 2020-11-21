from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def noti(request):
    return render(request,'notifications/noti.html')
