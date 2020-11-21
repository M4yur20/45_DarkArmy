from django import forms
from .models import Doctor,Patient,Agent

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['first_name','last_name','contact_no','email_id']

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['first_name','last_name','contact_no','email_id']

class AgentForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields=['first_name','last_name','contact_no','email_id']

    