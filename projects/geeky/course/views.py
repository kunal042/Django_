from django.shortcuts import render
from django.http import HttpResponse

def course_home(request):
    s = "This is the course page "
    return HttpResponse(s)
