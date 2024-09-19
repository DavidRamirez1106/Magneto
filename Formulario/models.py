from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Register (models.Model):
    name = models.CharField (max_length=100)
    email= models.EmailField()
    username= models.CharField(max_length=100, unique=True)
    password= models.CharField(max_length=128)



