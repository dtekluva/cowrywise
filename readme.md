
===================
 Django UUID App For CowryWise
===================

CowryWise :: https://cowrywise.com/blog/
   
Django application for CowryWise Opening.
App simply creates a new UUID and date every time a get request is sent  and then returns it all as a JSON


Getting Started
===============

Create and activate virtual environment using either :
- PIPENV
- VIRTUALENV

Clone repository, and install requirements

Requirements
============

CowryWise requires Django 2.2 or later and python3.7 or later.


Getting It
==========

You can get Django Extensions by using pip::

    $ pip install django
or 

`pip install -r requirements.txt`

If you want to install it from source, grab the git repository from GitHub and run setup.py::

    $ git clone https://github.com/dtekluva/cowrywise.git

Installing It
=============

To begin using the `cowrywise` project on your laptop you need to add it to `cd` into the your project and run the following commands::

    $ cd cowrywise
    $ python manage.py makemigrations 
    $ python manage.py migrate

This will create the required Database structure `SQLITE` in this case.

Using It
========

Run the django runserver command::

    $ python manage.py runserver

Visit localhost:8000/uuids/

Voila you're done.