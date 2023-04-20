### install virtualenv

```sh
pip install virtualenv
```

### create virtualenv

```sh
virtualenv env or python -m virtualenv env
```

### activate env -> in CMD not in Powershell

```
env\Scripts\activate.bat
```

### install django

```sh
pip install django
```

### create django project

```sh
django-admin startproject mysite
```

### run server

```sh
cd mysite
python manage.py runserver
```

### create app

```sh
python manage.py startapp base
```

### install app

1. Go to settings.py in the mysite foler
2. Add the appname in the intalled apps

### working with app

1. Create urls.py inside base app
2. paste the code

```py
from django.urls import path
from . import views

urlpatterns = [
    path("base/",views.base)
]

```

3. In the base/views.py

```py
from django.http import HttpResponse

def base(request):
    return HttpResponse("base!!!")

```

4. In mysite/urls.py include update urlpatterns

```py

path("app/",include("base.urls"))

```

5. Save all the changes and visit http://localhost:8000/app/base

# Django Models

### 1. Create a Model inside base/models.py

```py

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :

        return self.title

```

### 2. Create Table

```sh
python manage.py makemigrations
```

### 3. Push Table to db

```sh
python manage.py migrage
```

### 4. Create Superuser

```sh
python manage.py createsuperuser
```

# Access admin page

Go to /admin
