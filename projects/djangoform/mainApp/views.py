from django.shortcuts import render
from .forms import StudentRegistration


def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'mainapp/form.html', {"form":fm})