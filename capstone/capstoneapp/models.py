from __future__ import unicode_literals
from datetime import date

from django.db import models

# Create your models here.

class Doctor(models.Model):
    doc_id = models.CharField(max_length=20, default='', blank= True)
    password = models.CharField(max_length=20, default='', blank= True)

class Patient(models.Model):
    patient_id = models.CharField(max_length=20, default='', blank= True)
    first_name = models.CharField(max_length=30, default='', blank= True)
    last_name = models.CharField(max_length=30, default='', blank= True)
    GENDER = (('M','Male'),('F','Female'))
    gender = models.CharField(max_length=1, choices=GENDER)
    email = models.CharField(max_length=50, default='', blank= True)
    password = models.CharField(max_length=20, default='', blank= True)

class Disease(models.Model):
    name = models.CharField(max_length=30, default='', blank= True)
    parameter = models.CharField(max_length=30, default='', blank= True)

class Report(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    report_id = models.CharField(max_length=20, default='', blank= True)
    date = models.DateField(auto_now=True)
    measurement = models.CharField(max_length=1000, default='', blank= True)
    prediction = models.CharField(max_length=1000, default='', blank= True)
    suggestion = models.CharField(max_length=1000, default='', blank= True)
    comments = models.CharField(max_length=1000, default='', blank= True)

class Measurement(models.Model):
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
    age = models.IntegerField(default=0, blank= True)
    height = models.FloatField(default=0.0, blank= True)
    weight = models.FloatField(default=0.0, blank= True)
    pregnancies = models.IntegerField(default=0, blank= True)
    glucose = models.IntegerField(default=0, blank= True)
    insulin = models.IntegerField(default=0, blank= True)
    blood_pressure = models.IntegerField(default=0, blank= True)
    skin_thickness = models.IntegerField(default=0, blank= True)
    bmi = models.FloatField(default=0.0, blank= True)
    diabetes_predigree_function = models.FloatField(default=0.0, blank= True)
    heartbeat = models.IntegerField(default=0, blank= True)

# class Comment(models.Model):