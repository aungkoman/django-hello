# Django Cheat Sheet

## Create Django Project 

```bash
# step 1
# create django project
# mysite is project name 
django-admin startproject mysite

# step 2
# go to django project and run
cd mysite
python manage.py runserver


# step 3
# open http://127.0.0.1:8000/ in browser
# you can see landing page
```

## Create Django App
```bash
# step 1
# create django app
# tdl is app name
python manage.py startapp tdl

# step 2
# create urls.py file inside tdl folder
# type following code in tdl/urls.py
```

```tdl/urls.py```
```python
from django.urls import path

from . import views

urlpatterns = [ ]
```

```bash
# step 3
# to link urls file => update code in mysite/urls.py as follow
```

```mysite/urls.py```

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # this is new line to add
    path("tdl/", include("tdl.urls")),
    path("admin/", admin.site.urls),
]
```

```bash
# step 4 
# to link config file => update code in mysite/settings.py as follow
```
```mysite/settings.py```
```python
INSTALLED_APPS = [
    # this is new line to add
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

```bash
# completely added  
```

```