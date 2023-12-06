- To get a list of all the useful commands, use `django-admin`
- We created a new application using `django-admin startproject <project-name>`
- To create a new application in the project directory use `python3 manage.py startapp <app-name>`
- A single project can have multiple apps with its own components that are similar to the base project.

- The `manage.py` file that is present at the base level allows us to run command line commands.
- In the `view.py` we write the logic of what we want to do when the user goes to a certain page.
  - We have to map a url to the view function with the logic defined.
  - For that we need to create a `urls.py` file in the app directory, it would be similar to project level url file.
  - We need to import the view from the views to the url file and define that in the urls pattern ,we use name argument of paths like "appname-page" so different apps can have same routes but not collide.
  - Once we have that mapped we still need to tell the project urls which urls to direct to our app urls using the snippet, `path('appname/', include('appname.urls'))`
- It's a good idea to leave the trailing slashes in the urlpatterns of the main app so that with and without both work for a user.
- If we want to make one of the applications as the home for our project then we can change the name from something like `app/` to empty string `""` and it becomes the default home.

- By default in each application django looks for templates to find the html files that might be mentioned in the application views. **_blog -> templates -> blog -> .html files_**
- We have to add our application to our list of installed apps so that django knows to look for templates directory.

  - So we have to add app configuration to our project `settings.py` module.
  - The app configuration is location in the application's `apps.py` module.
  - `<appname>Config` from `apps.py` is added to `settings.py` file in project under `INSTALLED_APPS` list.

- We can pass context as third argument in render templates. That can pass information variables to template html.
  - Then we can access that variable in the page using jinja template.
- When creating templates it is better to create base template and use code blocks so that multiple pages can access that same html code that they share.
  - We create block using `{% block <content_name> %}`.
  - Then we remove the common code in the child pages and using `{% extends <path to base.html> %}` and overwrite base block using `{% block <content_name> %}`
  - Templating is useful as we can add something like bootstrap to just base and every child page would inherit it.
  - Also to use css we need to create static directory similar to template structure that contains all the css code. Then we can use `{% load static %}` at the top of base html page to load the css.
  - Then we can use the css using `<link rel="stylesheet", type="text/css" href="{% static '<appname>/main.css%}">`, static here creates an absolute path.
- For urls to pages, rather than hardcoding the hrefs it's better to use `{% url 'name-of-view' %}` as it change and we don't have to change it everywhere.

- First we have to create a database using migrate

  - `python manage.py makemigrations`
  - `python manage.py createsuperuser`
  - Login to the admin page using `localhost:8000/admin/login`

- In Django, ORM stands for Object-Relational Mapping. It is a technique that allows you to interact with your database using Python objects instead of raw SQL queries. The ORM in Django provides a high-level, Pythonic way to interact with databases, making it more abstract and easier for developers to work with databases in their web applications.
- In `models.py` we can add our models, each individual classwould be a separate table.
- When we create models we need to update the database using the migrations. We can checkout the SQL that it will run on migration using this command `python manage.py sqlmigrate <appname> <0001 (whatever number)>`
- To migrate we can run `python manage.py migrate`.

- We can interact with the ORM using the shell.

  - To open the shell using `python manage.py shell`.
  - Then import the models and User
    ```
    from <appname>.models import <modelName>
    from django.contrib.auth.models import User
    ```
  - Then we can list all objects using `User.objects.all()`, `User.objects.first()`, `User.objects.last()`, `User.objects.filter(<condition>)`, `User.objects.get(id=<user_id>), `etc.
  - We can assign them to variables which make them easier to use like, `User.objects.filter(username="username").first()`.
  - List user id using `user.id` or `user.pk`.
  - We can also query other models like `<modelName>.objects.all()`
  - We can also create new entries, like if we have blog post as new model then we can create new entry using:
    - `post_1 = Post(title="blog 1", content="first post content", "author"=user)`
    - `post_1.save()`

- We can also check the model set using the attribute like this:

  - `user = User.objects.get(id=1)`
  - `user.post_set`
  - We can also create new post without having to explicitly use `.save` function.
    - `user.post_set.create(title="blog 3", content = "third post content")`

- To see the created models into the admin page with Groups and Users then we should add it to admin page under <appname>/admin.py using `admin.site.register(modelName)`.

- To not have to reinvent the wheel we can use UserCreationForm() from django.contrib.auth.forms for user form views.
- In forms we create conditions so that if the data is being sent then we can do something with that, otherwise we just open the user register form.

  - We have also used the redirect function from django.shortcuts and put the url name to redirect to a given page. Also we have used `form.save` to save the user easily that we can check from the admin page.
    ```
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
    ```

- To add more details to the user form we can add something like a new email field, for that we have to create a new form which inherits from the user form.

- For login we can use the default views that django provides builtin from the auth module importing `from django.contrib.auth import views as auth_views` then we can use it as `path("login/", auth_views.LoginView.as_view(), name="login")` similar for logout as well.
- For the login page template it looks for it in the `registration/login.html` path so we have to create it there, but we can make change in the url pattern to make it look elsewhere where we want it to.
- We would need to add `accounts/profile` as the user when logged in needs to be directed to this url. But we added a main setting `LOGIN_REDIRECT_URL = "blog-home"` to make it redirect to home page.
- When we have all the login logout register pages ready then we can use conditionals to change the links in the navigation bar or anywhere else to show login and register when user is logged out else show logout.
  ```
  {% if user.is_authenticated %}
      <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'logout'%}">Logout</a>
      </li>
  {% else %}
      <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'login'%}">Login</a>
      </li>
      <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'register'%}">Register</a>
      </li>
  {% endif %}
  ```
- In the same conditional alongside the logout we can also display link to profile page, we created another view in users application. But the problem is that we can logout but still can navigate to profile page manually although it might be shown blank but navigation to it shouldn't be possible on logout.

  - We can use the `@login` decorator that django already provides.
  - Adding this decorator make django look for the user login page at `/accounts/login/?next=/profile/` but as done previously we can change this in main settings `LOGIN_URL = "login"`.
  - On the login page then it keeps track that next after login it has to go to the profile page by itself `http://localhost:8000/login/?next=/profile/`

- For user profile functionality we need to extend the user model in django in the `users/models.py`. There needs to be one-to-one funtionality.

  - We have to create a model similar to how we create a post.

  ```
  from django.contrib.auth.models import User

  class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      image = models.ImageField(default='default.png', upload_to='profile_pics')

      def __str__(self):
          return f"{self.user.username} Profile"
  ```

  - Then we have to makemigrations and migrate to make changes to the database.
  - We also need to register it in the app's `admin.py`, this is done so that it is accessble to the admin portal.

    ```
    from .models import Profile

    admin.site.register(Profile)
    ```

- We can access the shell here as well using `python3 manage.py shell` and we can access the multiple attributes attached to each user.

  ```
  from django.contrib.auth.models import User
  user = User.objects.filter(username="prashantbrahmbhatt")
  ```

  - `user.profile`
  - `user.profile.image`
  - `user.profile.image.width`
  - `user.profile.image.height`
  - `user.profile.image.size`

- In order to manage the paths and directories of the profile pictures stored we have to change the project settings in the project `settings.py` file.

  ```
  MEDIA_ROOT = os.path.join(BASE_DIR, "media") # Base is already defined, <dirname> we can add as per our naming.

  MEDIA_URL = "/media/" # <dirname>
  ```

- For non-deployment strategy we have to define in the projects `urls.py` this:
  ```
  if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
- We are going to create a `signals.py` in our users app. This would be used so that when a new user is created there is automatically a profile created for the user.

  - When a user is saved then send this signal, the signal is received by this receiver.

  ```
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from .models import Profile

  @receiver(post_save, sender=User)
  def create_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)


  @receiver(post_save, sender=User)
  def save_profile(sender, instance, **kwargs):
      instance.profile.save()
  ```

  - We also have to register this under User config in `apps.py`.

  ```
  class UsersConfig(AppConfig):
  default_auto_field = "django.db.models.BigAutoField"
  name = "users"

  def ready(self):
      import users.signals
  ```

- For User profile updation we need to add two separate forms for information update and profile picture update.

  ```
    from .models import Profile

    class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

    class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ["image"]
  ```

  - Then we need to update our views to allow these updates.

  ```
    @login_required
    def profile(request):
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()

        context = {
            "u_form": u_form,
            "p_form": p_form
        }

        return render(request, "users/profile.html", context)
  ```

  - Then we can simply access the variables `{{ u_form|crispy }}` and `{{ p_form|crispy }}` in our templates.
  - But it is important that in the template the form element has enctype defined as `<form method="POST", enctype="multipart/form-data"` otherwise the picture may not get saved in the backend.

- We might want to have prefilled the current information in the profile form we want to update. For that we can just update the view to have these instances.

  ```
  u_form = UserUpdateForm(instance=request.user)
  p_form = ProfileUpdateForm(instance=request.user.profile)
  ```

  - For updation if the request is post we need to save it accordingly.

  ```
  if request.method == "POST":
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect("profile")
  ```

- For allowing efficient use of large profile images for profile pictures we can override the save method in our profile model which would look now like this:

  ```
  class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default="default.png", upload_to="profile_pics")

  def __str__(self):
      return f"{self.user.username} Profile"

  def save(self):
      super().save()

      img = Image.open(self.image.path)
      if (img.height > 300) or (img.width > 300):
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save()
  ```

- We can replace our function home view to a new view that inherits the built in view called `ListView`.

  ```
    from django.views.generic import ListView
    class PostListView(ListView):
        model = Post
        template_name = "blog/home.html" # this needs to be there otherwise it looks for a default template at default path. <app>/<model>_<viewtype>.html
        context_object_name = "posts"
        ordering = ["-date_posted"] # this will change the ordering of the content as per the date
  ```

  - But we would also have to update our app url from `path("", views.home, name="blog-home"),` to `path("", PostListView.as_view(), name="blog-home"),`.

- Now we need to create detailed view so that we can open individual content. For that we would use the `DetailView` in the `views.py`.

  ```
  class PostDetailView(DetailView):
  model = Post
  ```

  - We accordingly need to create the app url for that which can dynamically fetch different content.
    `path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")`
  - And in our template we need to use `object.<attribute>` to refer to model instance attributes, so it will be like `object.title`, `object.content`, etc.

- We have to make a create blog view that allows the user to create a new content post. For that we would use the inbuilt `CreateView` provided by django.

  - We have created the `form_valid` function that overrides the default, we have used this so that an author is attached to the post before it gets saved and no author error is resolved. We also have to update our model to include this function:
    ```
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    ```
  - `LoginRequiredMixin` makes it redirect to log in page if the user is not logged in.

    ```
    from django.contrib.auth.mixins import LoginRequiredMixin

    class PostCreateView(LoginRequiredMixin, CreateView):
        model = Post
        fields = ["title", "content"]

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
    ```

    - For any updation deletion of objects we need to pass in `object.id` in our templates url so that it knows which object to perform operations on. Like this `{% url 'post-update' object.id %}`

- Similar to other views we can also create a delete view with proper template.

  - The `success_url` is there to make sure there is a path to redirect to after deletion

    ```
    class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post

        success_url = "/"
        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False
    ```

- To implement pagination let's see how paginator works and what functions can we leverage:

  ```
  >>> from django.core.paginator import Paginator
  >>> posts = ['1', '2', '3', '4', '5']
  >>> p = Paginator(posts, 3)
  >>> p.num_pages
  >>> 2
  >>> for page in p.page_range:
  >>> ... print(page)
  >>> ...
  >>> 1
  >>> 2
  >>> p1 = p.page(1)
  >>> p1
  >>> <Page 1 of 2>
  >>> p1.number
  >>> 1
  >>> p1.object_list
  >>> ['1', '2', '3']
  >>> p1.has_previous()
  >>> False
  >>> p1.has_next()
  >>> True
  >>> p1.next_page_number()
  >>> 2
  >>>
  ```

  - For implementation in the app first we go to the`views.py`in the blog and modify the post view by adding`paginate_by`.

  ```
    class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = [
    "-date_posted"
    ] # this will change the ordering of the content as per the date
    paginate_by = 5

  ```

  - Then we just modify the template to add the pagination buttons.

  ```

  {% if is_paginated %}
  {% if page_obj.has_previous %}
  <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
  <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
  {% endif %}
  {% for num in page_obj.paginator.page_range %}
  {% if page_obj.number == num %}
  <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
  {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
  <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
  {% endif %}
  {% endfor %}
  {% if page_obj.has_next %}
  <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
  <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
  {% endif %}

  {% endif %}

  ```

- We can also implement pagination for each user where click on username would only show posts by that user for that we would also create a `ListView` similar to posts one with one function `get_queryset` overridden.

  ```
  from django.shortcuts import get_object_or_404
  from django.contrib.auth.models import User

  class UserPostListView(ListView):
      model = Post
      template_name = "blog/user_posts.html"
      context_object_name = "posts"
      paginate_by = 5

      def get_queryset(self):
          user = get_object_or_404(User, username=self.kwargs.get("username"))
          return Post.objects.filter(author=user).order_by("-date_posted")
  ```

  - Then we create a url for the user posts.

  ```
      `path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),`
  ```

  - Finally we add the url with username passed in the template.

  ```
      <a class="mr-2" href="{% url 'user-posts' post.author.username %}">{{ post.author }}</a>
  ```
