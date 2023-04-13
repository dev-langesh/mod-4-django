### install virtualenv

pip install virtualenv

### create virtualenv

virtualenv env or python -m virtualenv env

### activate env -> in CMD not in Powershell

env\Scripts\activate.bat

### install django

pip install django

### create django project

django-admin startproject mysite

### run server

1. cd mysite
2. python manage.py runserver

### create app

python manage.py startapp base

### install app

1. Go to settings.py in the mysite foler
2. Add the appname in the intalled apps

### working with app

1. Create urls.py inside base app
2. paste the code

```

from django.urls import path
from . import views

urlpatterns = [
    path("base/",views.base)
]

```

3. In the base/views.py

```
from django.http import HttpResponse

def base(request):
    return HttpResponse("base!!!")

```

4. In mysite/urls.py include update urlpatterns

```

path("app/",include("base.urls"))

```

5. Save all the changes and visit http://localhost:8000/app/base
