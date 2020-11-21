from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Agent)
admin.site.register(Hospital)