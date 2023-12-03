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

$ pip install django-crispy-forms

$ pip install crispy-bootstrap5
