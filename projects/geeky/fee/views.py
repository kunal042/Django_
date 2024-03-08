from django.shortcuts import render
from django.http import HttpResponse

def sample(request):
    a = "<h1> Hello Django!!"
    return HttpResponse(a)


def about(reuest):
    x = "<h1>This is about Page!! </h1>"
    return HttpResponse(x)


def contact(reuest):
    x = "<h1>This is Contact Page!! </h1>"
    return HttpResponse(x)