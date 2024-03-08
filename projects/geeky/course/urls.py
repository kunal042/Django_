from django.urls import path

from . import views

urlpatterns = [
    path("c_u", views.course_home),
]

