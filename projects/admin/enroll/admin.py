from django.contrib import admin
from enroll.models import Student



@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('studid', 'studname', "studemail", "studpass" )


# admin.site.register(Student, StudentAdmin)