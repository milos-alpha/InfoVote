from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)  
    email = models.EmailField(unique=True)  

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['full_name', 'username']

    def __str__(self):
        return self.email
    
    
class Voter(models.Model):
    full_name = models.CharField(max_length=255) 
    username = models.CharField(max_length=255)  
    email = models.EmailField(unique=True)  
    residence = models.CharField(max_length=255) 
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.CharField(max_length=255) 
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username