from django.contrib import admin
from .models import Student




class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'stuid', 'stuname', 'stuemail', 'stupass', 'comment']

admin.site.register(Student, StudentAdmin)