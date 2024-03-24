from django.shortcuts import render
from .forms import StudentRegistration


def showformdata(request):
    fm = StudentRegistration(auto_id=True, label_suffix="  ", initial={
                             "name": "Kunal", 'email': "kunal@outlook.com"})
    fm.order_fields(field_order=['first_name', 'name', 'email'])
    return render(request, 'mainapp/form.html', {"form": fm})
