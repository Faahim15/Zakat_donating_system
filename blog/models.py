from django.db import models 
from django.contrib.auth.models import User 
from django.utils import timezone 
from datetime import datetime
# Create your models here.
class Projects(models.Model):
    img = models.ImageField(upload_to="donations/media/images/",null = True,blank=True)
    title = models.CharField(max_length = 50) 
    description = models.TextField()
    progress = models.PositiveIntegerField()
    goal = models.PositiveIntegerField() 
    class Meta:
        verbose_name_plural = "Projects"
    def __str__(self):
        return f"{self.title}"

class Donations(models.Model):
    provide_to = models.ForeignKey(Projects, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    class Meta:
        verbose_name_plural = "Donations"

    def __str__(self):
        return f"Donation of {self.amount} to {self.provide_to}"
       
    

class BlogPost(models.Model):
    title = models.CharField(default = 'Zakat donations',max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField() 
    class Meta:
        verbose_name_plural = "Blog Post"
    def __str__(self):
        return f"{self.author}"





