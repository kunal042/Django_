from django.db import models

class Student(models.Model):
    studid = models.IntegerField()
    studname = models.CharField(max_length=70)
    studemail = models.EmailField(max_length=70)
    studpass = models.CharField(max_length=70)
    
    def __str__(self):
        return str(self.studid) +"/" + self.studname