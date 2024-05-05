from django.contrib import admin
from .models import user


@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', "teacher_name", 'email', 'password']
