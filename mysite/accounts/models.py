from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    email_id=models.EmailField()

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    email_id=models.EmailField()

class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    email_id=models.EmailField()
