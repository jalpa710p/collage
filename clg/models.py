from django.db import models 

# Create your models here.

class Collage(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=15)
    Birthdate = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    High_school = models.CharField(max_length=30)
    Essay = models.CharField(max_length=100)
    img = models.ImageField(upload_to="jalpa/")

