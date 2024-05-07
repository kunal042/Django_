from django.shortcuts import render, HttpResponseRedirect
from .form import SignUpForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User, Group
# Create your views here.


def sign_up(request):

    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Create Sucessfully!!")
            user = fm.save()
            group = Group.objects.get(name='Editior')
            user.groups.add(group)
        # fm = SignUpForm()

    else:
        fm = SignUpForm()

    return render(request, "enroll/signup.html", {"form": fm})


# login views function

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Loggedin Successfully!!")
                    return HttpResponseRedirect("/dashboard/")
        else:
            fm = AuthenticationForm()
        return render(request, "enroll/userlogin.html", {"form": fm})
    else:
        return HttpResponseRedirect("/dashboard/")


# Dashboard

def user_dashboard(request):

    if request.user.is_authenticated:
        return render(request, "enroll/dashboard.html", {"name":request.user.username})
    else:
        return HttpResponseRedirect("/dashboard/")

# logout


def user_logout(request):
    logout(request)

    return HttpResponseRedirect("/login/")





def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, "enroll/userdetails.html", {"form":fm} )
    else:
        return HttpResponseRedirect("/login/")