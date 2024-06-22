from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     user_name = models.CharField(max_length=100)
#     password  = models.CharField(max_length=100)


class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff' :True})
    page_name = models.CharField(max_length=100)
    page_cat = models.CharField(max_length=100)
    page_publish_date = models.DateField()


