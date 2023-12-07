from django.contrib import admin

from .models import Expense, ExpenseTypes

admin.site.register(ExpenseTypes)
admin.site.register(Expense)