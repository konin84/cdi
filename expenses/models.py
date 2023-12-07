from django.db import models

class ExpenseTypes(models.Model):
    name = models.CharField(max_length=300, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    expense = models.ForeignKey(ExpenseTypes, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.expense
    

