from django.db import models
from insurance.models import Insurance
# Create your models here.
from account.models import UserAccount


class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", 'Male'
        FEMELE = "FEMELE", 'Femele'
        OTHER = "OTHER", 'Autre'

    gender = models.CharField(max_length=15, choices=Gender.choices)

    insurance = models.ForeignKey(Insurance, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    profession = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    insurance_matricule = models.CharField(max_length=200)
    insurance_pourcentage = models.IntegerField()
    email = models.EmailField( max_length=150, verbose_name='email address')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} - {self.lastname}'


class PatientMessage(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
  subject = models.CharField(max_length=200)
  message = models.TextField()

  updated_on = models.DateTimeField(auto_now=True)
  registered_on = models.DateTimeField(auto_now_add=True)
  class Meta:
        ordering = ['-registered_on']

  def __str__(self):
        return f'{"Message N°"}-{self.id} - {self.subject}'

