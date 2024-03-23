from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    studname = models.CharField(max_length=70)
    studemail = models.EmailField(max_length=70)
    studemail = models.CharField(max_length=70)
