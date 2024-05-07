from django.shortcuts import render, HttpResponseRedirect
from .form import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

# Create your views here.


def sign_up(request):

    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Create Sucessfully!!")
            fm.save()
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
                    return HttpResponseRedirect("/profile/")
        else:
            fm = AuthenticationForm()
        return render(request, "enroll/userlogin.html", {"form": fm})
    else:
        return HttpResponseRedirect("/profile/")


# profile

def user_profile(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, "Data  Changed Sucessfully!!")
                fm.save()
                return HttpResponseRedirect("/profile/")
        else:
            fm = EditUserProfileForm(instance=request.user)
            return render(request, 'enroll/profile.html', {"name": request.user, "form": fm})
    else:
        return HttpResponseRedirect("/profile/")

# logout


def user_logout(request):
    logout(request)

    return HttpResponseRedirect("/login/")


# Change password with old password

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed Sucessfully!!")
                return HttpResponseRedirect("/profile/")
        else:
            fm = PasswordChangeForm(user=request.user)

        return render(request, "enroll/changepass.html", {'form': fm})
    else:
        return HttpResponseRedirect("/login/")


# Change password without old password

def change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, "Password Changed Sucessfully!!")
                return HttpResponseRedirect("/profile/")
        else:
            fm = SetPasswordForm(user=request.user)

        return render(request, "enroll/changepass1.html", {'form': fm})
    else:
        return HttpResponseRedirect("/login/")
