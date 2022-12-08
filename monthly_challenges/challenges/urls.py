# This file contains the urls for the app
from django.urls import path

# importing the view file from the same folder as the current urls file exist
from . import views

urlpatterns = [
    # it means that if a request reaches /january then execute this index view function, this creates a url config
    path("january", views.january),
    path("february", views.february),
]
