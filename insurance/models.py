from django.db import models

# Create your models here.


class Insurance(models.Model):
    insurancename = models.CharField(max_length=300, unique=True, primary_key = True)
    telephone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        max_length=150, unique=True, verbose_name='email address')
    address = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.insurancename
