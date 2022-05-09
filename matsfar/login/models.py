import email
from django.db import models

# Create your models here.

class intel(models.Model):
    name =models.CharField(max_length=100)
    Det =models.CharField(max_length=255)
    email ==models.CharField(max_length=255)


