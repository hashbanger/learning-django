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

- By default in each application django looks for templates to find the html files that might be mentioned in the application views. **blog -> templates -> blog -> .html files**
- We have to add our application to our list of installed apps so that django knows to look for templates directory.

  - So we have to add app configuration to our project settings.py module.
  - The app configuration is location in the application's apps.py module.
  - <AppName>Config from apps.py is added to settings.py file in project under INSTALLED_APPS list.

- We can pass context as third argument in render templates. That can pass information variables to template html.
  - Then we can access that variable in the page using jinja template.
- When creating templates it is better to create base template and use code blocks so that multiple pages can access that same html code that they share.
  - We create block using {% block <content_name> %}.
  - Then we remove the common code in the child pages and using {% extends <path to base.html> %} and overwrite base block using {% block <content_name> %}
  - Templating is useful as we can add something like bootstrap to just base and every child page would inherit it.
  - Also to use css we need to create static directory similar to template structure that contains all the css code. Then we can use {% load static %} at the top of base html page to load the css.
  - Then we can use the css using <link rel="stylesheet", type="text/css" href="{% static '<app_name>/main.css%}">, static here creates an absolute path.
- For urls to pages, rather than hardcoding the hrefs it's better to use {% url 'name-of-view' %} as it change and we don't have to change it everywhere.
