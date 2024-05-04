from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from.models import user

# Create your views here.

# This Function will Add new items and show All Items 
def add_show(request): 
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            print(nm, em, pw)
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = user.objects.all()
    
    
    return render(request, 'enroll/addnshow.html',  {'fm':fm,  'stu' : stud})

# This  function will update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration( instance=pi)

    return render(request, 'enroll/updatestudent.html',  {'form':fm})


# This Function will be Delete?
def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect("/")
