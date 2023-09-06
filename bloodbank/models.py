from django.db import models

# Create your models here.
class BloodSample(models.Model):
    blood_group=models.CharField(max_length=5)
    doner=models.CharField(max_length=30)
    