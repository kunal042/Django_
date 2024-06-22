from django.db import models


class CustomManger(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by('name')
    
    

class CustomManger2(models.Manager):
    def get_stu_roll_range(self,r1,r2) -> models.QuerySet:
        return super().get_queryset().filter(roll__range=(r1,r2))
    
