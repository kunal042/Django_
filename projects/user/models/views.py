from django.shortcuts import render

from models.models import Student


def student_info(request):
    stud = Student.objects.all()
    
    return render(request, "models/student.html", {"stu":stud} )
