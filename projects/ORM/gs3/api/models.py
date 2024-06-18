from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=40)
    marks = models.IntegerField()
    passdate = models.DateField()
    admdatetime = models.DateTimeField()
    
      
