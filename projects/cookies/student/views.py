from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def get_cookies(request):
    # name = request.COOKIES["name"]
    # name = request.COOKIES.get("name")
    name = request.COOKIES.get("name", "By Default Value of cookies if Delete")
    return render(request, "student/getcookies.html", {'name':name})

def set_cookies(request):

    response =  render(request, 'student/setcookies.html')
    # response.set_cookie('name', "sonam", max_age=120)
    response.set_cookie('name', "sonam", expires=datetime.utcnow() + timedelta(days=2) )
    return response

def del_cookies(request):

    response = render(request, 'student/delcookies.html')
    response.delete_cookie('name')
    return response
