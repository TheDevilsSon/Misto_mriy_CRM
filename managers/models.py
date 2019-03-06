from django.db import models

# Create your models here.
class Manager(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
