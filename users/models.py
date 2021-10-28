from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
    )
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField(verbose_name='возраст',null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255)
    
    def __str__(self):
        return f'{self.username}==={self.age}'