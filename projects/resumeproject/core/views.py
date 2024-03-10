from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {"home" : "active"}
    return render(request, "core/index.html", context)


def contact(request):
    context = {"contact" : "active"}

    return render(request, "core/contact.html", context)
