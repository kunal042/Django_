from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

# Create your views here.


def home(request):

    exam_center = ExamCenter.objects.all()
    my_exam_center = MyExamCenter.objects.all()

    context = {
        'exams' : exam_center,
        'myexams' : my_exam_center
    }

    return render(request, 'school/home.html', context)
