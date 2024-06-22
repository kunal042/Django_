from django.contrib import admin
from .models import  User, Page

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['user_name', 'password']
    

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user', 'page_name', 'page_cat', 'page_publish_date']
