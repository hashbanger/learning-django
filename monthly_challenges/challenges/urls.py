# This file contains the urls for the app
from django.urls import path

# importing the view file from the same folder as the current urls file exist
from . import views

urlpatterns = [
    # the order matters
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
