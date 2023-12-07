from django.contrib import admin

# Register your models here.
from .models import UserAccount, Accountant, Patient, Doctor, Cashier, Administrator

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Administrator)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Accountant)
admin.site.register(Cashier)
