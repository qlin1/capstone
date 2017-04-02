from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)