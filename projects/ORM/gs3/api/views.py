from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    student_data = Student.objects.all()
    print("Return", student_data)
    print("")
    print("SQL  Query :" , student_data.query )
    return render(request, 'api/home.html', {"student":student_data})
