# System-Development-Backend

This project was generated with [Django](https://www.djangoproject.com/) version 3.1.5.

## Installing Dev Dependencies

* Run `pip install -r requirements.txt` to install the dependencies.
* Run `python manage.py makemigrations` to make migration files from models.
* Then run `python manage.py migrate` to create the actual database tables.
* You can run `python manage.py check` to look for any errors.

## Development Server

* Run `python manage.py runserver` for a dev server.
* Navigate to http://localhost:8000/ to view the app.
* User `Ctrl + C` or `Ctrl + pause/break` to shut down the server.

## Accessing the Admin Panel

* Run `python manage.py createsuperuser` from the terminal.
* Give some `username, email and password`.
* Go to http://localhost:800/admin/ to login to the admin panel.

## Running Unit Test

You can run `python manage.py test` to execute the unit tests.

## Further Help

To get more help on Django Command line run `python manage.py help` or go check out the [django-admin and manage.py](https://docs.djangoproject.com/en/3.1/ref/django-admin/) page.
