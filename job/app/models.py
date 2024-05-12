from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class jobs(models.Model):
    title=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    salary=models.CharField(max_length=100)
    desc=models.CharField(max_length=5000)
    image=models.ImageField(upload_to='pics')
    website_url = models.URLField(default=None)
    experiance=models.CharField(max_length=1000,default=None)
    education=models.CharField(max_length=1000,default=None)
    jobrole=models.CharField(max_length=100,default=None)
    