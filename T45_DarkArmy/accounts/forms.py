from django import forms
from .models import *


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'contact_no', 'email_id']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'contact_no', 'email_id', 'emergency_contact_no' , 'address']


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'contact_no', 'email_id']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name','contact','address']



