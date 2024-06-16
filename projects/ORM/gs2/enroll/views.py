from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def student(request):

    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=55)
    # student_data = Student.objects.exclude(marks=98)

    # student_data = Student.objects.order_by("-marks")
    # student_data = Student.objects.order_by("?") # random data show


    # student_data = Student.objects.order_by("id").reverse()
    # student_data = Student.objects.order_by("id").reverse()[:3]


    # student_data = Student.objects.values("name",'city')


    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id', 'name', named=True)
    
    # student_data = Student.objects.using("default")

    #student_data = Student.objects.dates("pass_date", 'month')


    #####################  Second 'Teacher" Started #################

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)

    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)

    # student_data = qs2.union(qs1, all=True)


    # ****************Intesection part***********************

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)

    # student_data = qs2.intersection(qs1)


    # ****************Difference part***********************

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)

    # student_data = qs1.difference(qs2)


    ### -----------And  Operator--------

    # student_data = Student.objects.filter(id=3) & Student.objects.filter(roll=104)
    # student_data = Student.objects.filter(id=3, roll=104) 
    # student_data = Student.objects.filter(Q(id=3) & Q(roll=3)) 


    ### -----------OR Operator--------
    # student_data = Student.objects.filter(id=2) | Student.objects.filter(roll=4) 
    student_data = Student.objects.filter(Q(id=3) | Q(roll=4)) 

    print('Return :', student_data)
    print()
    print('SQL Query Set :', student_data.query)

    return render(request, 'enroll/student.html', {'stud' : student_data})