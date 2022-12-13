from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page-path"),  # path for the index page
    path("posts", views.posts, name="posts-page-path"),  # path for posts
    path(
        "posts/<slug:slug>", views.post_detail, name="posts-detail-page-path"
    ),  # dynamic path for individual posts
]
