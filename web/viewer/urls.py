# Django Modules
from django.urls import path

# Project Modules
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
