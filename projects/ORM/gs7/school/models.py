from django.db import models
from .managers import CustomManger,CustomManger2

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    # students = models.Manager()

    # students = CustomManger()
    students = CustomManger2()




    