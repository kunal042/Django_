from django.shortcuts import render
from .models import Student, ExamCenter

# Create your views here.

def home(request):
    exam_center = ExamCenter.objects.all()
    Student_data = Student.objects.all()

    context = {
        'centers' : exam_center,
        'students' : Student_data,
    }

    return render(request, 'school/home.html', context )
