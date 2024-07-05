from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name = "app/student_list.html"
    template_name_suffix = "_list"
    ordering = ['course']

    def get_queryset(self):
        return Student.objects.filter(course='Django')
    
    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args,**kwargs)
        context["freshers"] =  Student.objects.all().order_by('name')
        return context
    
