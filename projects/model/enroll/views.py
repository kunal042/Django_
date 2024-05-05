from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
from .models import user


# Create your views here.

def home(request):
    fm = StudentRegistration()
    return render(request, 'enroll/index.html', {'form' :fm})

def student_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()

    else:
        fm = StudentRegistration()

    return render(request, 'enroll/student.html', {"form" : fm})

def teacher_form(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = TeacherRegistration()

    else:
        fm = TeacherRegistration()

    return render(request, 'enroll/teacher.html', {"form" : fm})

