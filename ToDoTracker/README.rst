-------------------
Infrastructure for the app
-------------------

Frameworks download.

Step 1:
Download and install pip in order to be able to download django via pip.

Follow the steps that are in the following site.
https://pip.pypa.io/en/latest/installing.html

Step 2:
Look up in the following link for the first option and install and download django.
https://www.djangoproject.com/download/

Step 3:
Download and install the following library.
https://github.com/yceruto/django-ajax

After the first 3 steps for the frameworks are done:

Run in the terminal: pip install --user django-todo/dist/django-todo-0.1.tar.gz
----------------------
Quick start in the app
----------------------

1. Add "ToDo" and "django_ajax" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'ToDo',
        'django_ajax',
    )

2. Include the ToDo URLconf in your project urls.py like this::

    url(r'^ToDo/', include('ToDo.urls', namespace='ToDo'))

3. Run `python manage.py migrate` to create the polls models.

5. Visit http://127.0.0.1:8000/ToDo/ to create your ToDo's.