from django.shortcuts import render
from .form import registration

 
# Create your views here.


def regi(request):
    if request.method == "POST":
        fm = registration(request.POST)
        if fm.is_valid():
            fm.save()
        fm =  registration()
        
    else:
        fm = registration()


    return render(request, 'enroll/index.html', {"form": fm})
