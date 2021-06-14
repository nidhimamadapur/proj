from django.db import models

# Create your models here.
class PatientModel(models.Model):
    name = models.CharField(max_length = 128)
    age = models.CharField(max_length = 128)
    dependents = models.CharField(max_length = 128)
    address = models.CharField(max_length = 128)
    healthIssues = models.CharField(max_length = 128)