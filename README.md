Django-Locations
================
Djnago-Location Provides you the all countries ,states and cities details over the world,this is not a plugin this is a reusable app for Django 1.7

Step 1: Clone Repo
------------------
Clone repo to your Project,this is a reusable app for django1.7 project
"git clone https://github.com/krishnadaszorse/Django-Locations.git"


Step 2: Update Settings.py
------------------
add 'location' to your INSTALLED_APPS in settings.py
"""
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ......
    'location',
)
"""

Step 3: Update urls.py
------------------
include 'location.urls' to your urlpatterns in urls.py
"""
urlpatterns += patterns('',
    url(r'^', include('location.urls')),
)
"""

Step 4: Migrate Database and Loaddata
------------------
"python manage.py migrate"
"python manage.py loaddata initial_data"