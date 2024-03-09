from django.shortcuts import render
from django.http import HttpResponse

def course_home(request):
    
    return render(request, "index.html", {"name":"kunal", "age":22, "city":"Gurgaon"})
