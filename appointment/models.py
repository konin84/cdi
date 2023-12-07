from django.db import models

from account.models import UserAccount
from patient.models import Patient


class Appointment(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
  patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
  status = models.CharField(max_length=100)
  commentaire = models.TextField()
  rendezvousdate = models.DateField()
  rendezvoustime = models.TimeField()
  updated_on = models.DateTimeField(auto_now=True)
  registered_on = models.DateTimeField(auto_now_add=True)
  class Meta:
        ordering = ['-registered_on']

  def __str__(self):
        return f'{"Rendezvous N°"}-{self.id} - {self.patient}'

