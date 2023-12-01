from django.shortcuts import render

# adding dummy data for templates
posts = [
    {
        "author": "PrashantB",
        "title": "Blog Post",
        "content": "first post content",
        "date_posted": "December 1, 2023",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second blog post",
        "date_posted": "December 1, 2023",
    },
]

# Create your views here.


# this function is going to take the traffic from the home page
def home(request):
    context = {"posts": posts, "title": "Home"}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
