

from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("home/", views.TemplateView.as_view(template_name = 'mainapp/home.html'), name="home"),
    path("home/", views.HomeTemplateView.as_view(extra_context={'course': 'Python'}), name="home"),
    path("home/<int:roll>", views.HomeTemplateView.as_view( ), name="home"),
]

