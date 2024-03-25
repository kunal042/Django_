from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

def suceess(request):
    return render(request, 'enroll/suceess.html')


def student(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("form is Validated")
            print("Name  :",fm.cleaned_data['name'])
            print("Roll  :",fm.cleaned_data['roll'])
            print("Price  :",fm.cleaned_data['price'])
            print("Rate  :",fm.cleaned_data['rate'])
            print("comment  :",fm.cleaned_data['comment'])
            print("Email  :",fm.cleaned_data['email'])
            print("Website  :",fm.cleaned_data['website'])
            print("Password  :",fm.cleaned_data['password'])
            print("Description  :",fm.cleaned_data['description'])
            print("Feddback  :",fm.cleaned_data['feedback'])
            print("Note  :",fm.cleaned_data['note'])


            print("Agreed  :",fm.cleaned_data['agree'])
            
            # return render(request, 'enroll/sucess.html', {"nm":"name"})
            return HttpResponseRedirect('/enroll/suceess')
            

    else:
        fm = StudentRegistration()
        print("YE get request se aaya h")

    return render(request, 'enroll/index.html', {"forms": fm})
