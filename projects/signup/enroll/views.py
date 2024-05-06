from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)

        if fm.is_valid():
            un = fm.cleaned_data['Usename']
            pw = fm.cleaned_data['Usename']
            cpw = fm.cleaned_data['Usename']
            reg = UserCreationForm(name=un, password=pw, cpassword=cpw)
            fm.save
        fm = UserCreationForm()

    else:
        fm = UserCreationForm()
    return render(request, 'enroll/signup.html', {"form":fm})
