from django.db import models

from account.models import UserAccount
from patient.models import Patient
from treatment.models import Treatment

class Payment(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
  patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
  treatment = models.ForeignKey(Treatment, on_delete=models.DO_NOTHING, null=True)
  treatmentamount = models.IntegerField(null=True, blank=True)
  partinsurance = models.IntegerField()
  partpatient = models.IntegerField()
  amountpaid = models.IntegerField()
  updated_on = models.DateTimeField(auto_now=True)
  registered_on = models.DateTimeField(auto_now_add=True)
  class Meta:
        ordering = ['-registered_on']

  def __str__(self):
        return f'{"Payment N°"}-{self.id} - {"du patient"} {self.patient.firstname}  {self.patient.lastname} {"avec N°"} {self.patient.id}'

