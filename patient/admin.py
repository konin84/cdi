from django.contrib import admin
from .models import Patient, PatientMessage
# Register your models here.
admin.site.register(Patient)
class PatientMessageAdmin(admin.ModelAdmin):
  list_display=['id', 'user', 'subject', 'message']
admin.site.register(PatientMessage, PatientMessageAdmin)