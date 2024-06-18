from django.shortcuts import render
from .models import Student
from datetime import date, time

# Create your views here.


def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact='Sonam')
    # student_data = Student.objects.filter(name__iexact='sonam')
    # student_data = Student.objects.filter(name__contains='a')
    # student_data = Student.objects.filter(id__in = [1,3])
    # student_data = Student.objects.filter(marks__in = [60,70])
    # student_data = Student.objects.filter(marks__gt = 50)
    # student_data = Student.objects.filter(marks__lte = 50)
    # student_data = Student.objects.filter(name__startswith="S")
    # student_data = Student.objects.filter(name__endswith="m")
    # student_data = Student.objects.filter(name__iendswith="m")
    # student_data = Student.objects.filter(passdate__range=("2024-01-1", '2024-06-10'))
    # student_data = Student.objects.filter(admdatetime__date=date(2024,3,30))
    
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2024,3,30))
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2024,3,30))


    # student_data = Student.objects.filter(passdate__year=2024)
    # student_data = Student.objects.filter(passdate__year__gte=2024)
    # student_data = Student.objects.filter(passdate__month=2)
    # student_data = Student.objects.filter(passdate__month__gte=2)
    # student_data = Student.objects.filter(passdate__day=2)
    # student_data = Student.objects.filter(passdate__day__gte=2)
    # student_data = Student.objects.filter(passdate__week=2)
    # student_data = Student.objects.filter(passdate__week__gte=2)

    # student_data = Student.objects.filter(passdate__week__day=2)
    # student_data = Student.objects.filter(passdate__quarter=2)


    # student_data = Student.objects.filter(admdatetime__time__gt=time(6,00))
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=26)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)


    
    student_data = Student.objects.filter(roll_isnull=False)




    print("Return", student_data)
    print("")
    print("SQL  Query :" , student_data.query )
    return render(request, 'api/home.html', {"students":student_data})
