from django.contrib import admin

# Register your models here.

from . models import Profile,Doctor,Patient,Agent

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Agent)