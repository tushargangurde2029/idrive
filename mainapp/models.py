from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.


class User_Data(models.Model):
    image=models.ImageField(default="none")
    temail= models.CharField(max_length=30,default="xxx@gmail.com")
    mobile_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=12,default="None")
    

class Drive_Data(models.Model):
    demail=models.CharField(max_length=30)
    filename=models.CharField(max_length=30,default="nothing")
    ext=models.CharField(max_length=10,default="nothing")
    files=models.FileField() 
    description=models.CharField(max_length=100,default="There is no description for the given File")
    fsize=models.CharField(max_length=15,default="0 bytes")