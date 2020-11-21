from django.db import models

# Create your models here.
from accounts.models import Treatment,Doctor,Patient

class Notification(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    accepted=models.BooleanField(default=False)
    treatment=models.ForeignKey(Treatment,on_delete=models.CASCADE)
    prediction=models.CharField(max_length=10,null=True)

