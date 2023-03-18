from django.db import models

# Create your models here.

class Emailinfo(models.Model):
    emailaddress=models.CharField(max_length=100)
    subject=models.CharField(max_length=1000)

