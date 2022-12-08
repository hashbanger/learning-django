# This file contains the urls for the app
from django.urls import path

# importing the view file from the same folder as the current urls file exist
from . import views

urlpatterns = [path("<month>", views.monthly_challenge)]
