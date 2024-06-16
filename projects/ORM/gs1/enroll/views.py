from django.shortcuts import render
from .models import Student

# Create your views here.
def studentinfo(request):

    stud = Student.objects.all()
    print(stud)

    return render(request , 'enroll/base.html', {"stud":stud})


