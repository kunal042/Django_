from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

# def student(request):

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
    # student_data = Student.objects.filter(Q(id=3) | Q(roll=4)) 



    ## Lookup in django


    # student_data = Student.objects.last()
    # student_data = Student.objects.latest("pass_date")
    # student_data = Student.objects.earliest("pass_date")


    # student_data = Student.objects.all()
    # # print(student_data.exists())


    # one_data = Student.objects.get(pk=2)
    # print(student_data.filter(pk=one_data.pk).exists())

    # print('Return :', student_data)

    # return render(request, 'enroll/student.html', {'st' : student_data})



# Methods that do not return new query sets.

def student(request):
    # student_data = Student.objects.create(name="Kunal", roll=6, city="Muz", marks=60, pass_date="2020-5-3" )


    # student_data, create = Student.objects.get_or_create(name="Sameer", 
    #     roll=7, city="Muz", marks=60, pass_date="2020-5-3" )
    

    # student_data = Student.objects.filter(pk=2).update(name="Kabir", marks=80)

    # student_data = Student.objects.update_or_create(id=5, name='Kunal', defaults={'name': 'Kohli'})

    # objs = [
    #     Student(id=9, name="spana", roll=9, city="puna", marks=90, pass_date='2022-9-23'),
    #     Student(id=10, name="neha", roll=10, city="goa",marks=50, pass_date='2022-9-2'),

    # ]

    # student_data = Student.objects.bulk_create(objs)

    

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = "Delhi"
        
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])



    # student_data  = Student.objects.in_bulk([1,2])
    # print(student_data)
    # print(student_data[1].name)
    # print(student_data[2].name)



    # student_data = Student.objects.get(pk=4)
    # print(student_data.delete())

    
    student_data = Student.objects.all()
    print(student_data.count())

    # print('Return :', student_data)
    print()

 
    return render(request, 'enroll/student.html', {'st' : student_data})
