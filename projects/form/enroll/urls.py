from django.urls import path
from enroll import views

urlpatterns = [
    path("stu/", views.student),
    path("suceess/", views.suceess),
]