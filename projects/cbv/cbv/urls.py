"""
URL configuration for cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.myviews, name="func"),
    path("cl/", views.MyView.as_view(name="Rahul"), name="cl"),
    path("subcl/", views.MyViewChild.as_view(), name="subcl"),

    path("home/", views.home, name="home"),
    path("homecl/", views.Homeclass.as_view(), name="homecl"),

    ################################

    path("about/", views.aboutfun, name="about"),
    path("aboutcl/", views.AboutClass.as_view(), name="aboutcl"),


    ##################################
    path("contact/", views.contact, name="contact"),
    path("contactcl/", views.ContactClass.as_view(), name="contactcl"),


    #########################3

    path("news/", views.news, {"templates_name" : 'mainapp/news.html'}, name="news"),
    path("news2/", views.news, {"templates_name" : 'mainapp/news2.html'}, name="news"),
    path("newscl/", views.NewsClass.as_view(templates_name = "mainapp/news.html"),name="news"),
    path("newscl2/", views.NewsClass.as_view(templates_name = "mainapp/news2.html"),name="news2"),
]
