from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name


class Hospital(models.Model):
    doctor = models.ManyToManyField(Doctor)
    name = models.CharField(max_length=100)
    
