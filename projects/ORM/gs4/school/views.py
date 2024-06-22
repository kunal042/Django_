from django.shortcuts import render
from .models import Student, Teacher, Contractor

# Create your views here.

def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    contractor_data = Contractor.objects.all()

    context = {
        "st" : student_data,
        "tr" : teacher_data,
        'ct' :contractor_data,
    }
    return render(request, 'school/home.html', context)
