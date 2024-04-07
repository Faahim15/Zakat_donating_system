from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
GENDER_CHOICES= [
    ('male','Male'),
    ('female','Female'),
    ('others','Others')
]
class Donator(models.Model):
    donator = models.OneToOneField(User,on_delete = models.CASCADE) 
    mobile_no = models.CharField(max_length =14) 
    country = models.CharField(max_length =50) 
    gender = models.CharField(max_length =50, choices = GENDER_CHOICES) 
    image = models.ImageField(upload_to="donations/media/images/",null = True,blank=True)


    def __str__(self):
        return f"{self.donator.first_name} {self.donator.last_name}" 
    