=============================
django-nupages
=============================

.. image:: https://badge.fury.io/py/django-nupages.png
    :target: https://badge.fury.io/py/django-nupages

.. image:: https://travis-ci.org/goldhand/django-nupages.png?branch=master
    :target: https://travis-ci.org/goldhand/django-nupages

.. image:: https://coveralls.io/repos/goldhand/django-nupages/badge.png?branch=master
    :target: https://coveralls.io/r/goldhand/django-nupages?branch=master

Pages application for django projects

Documentation
-------------

The full documentation is at https://django-nupages.readthedocs.org.

Quickstart
----------

Install django-nupages::

    pip install django-nupages

Then use it in a project::

    import django-nupages

Cookiecutter-project Integration
--------------------------------

### Initial Setup

.. code-block:: bash

    mkproject PROJECT_NAME
    pip install cookiecutter
    cookiecutter https://github.com/pydanny/cookiecutter-django.git

### Github Setup

.. code-block:: bash

    workon PROJECT_NAME
    cd PROJECT_NAME
    git init
    git add .
    git commit -m 'init'
    git remote add origin git@github.com:USER_NAME/REPO_NAME.git
    git push origin master

### Development Setup

.. code-block:: bash

    workon PROJECT_NAME
    cd PROJECT_NAME
    pip install -r requirements/local.txt
    npm install
    createdb PROJECT_NAME
    python PROJECT_NAME/manage.py syndb
    python PROJECT_NAME/manage.py migrate


### nupages Setup

.. code-block:: bash
    pip install git+https://github.com/goldhand/django-nupages.git
    # eventually will be pip install django-nupages

# add 'nupages' to PROJECT_NAME/config/settings.py in THIRD_PARTY_APPS (lines 47 - 51)

.. code-block:: python

    THIRD_PARTY_APPS = (
        'south',  # Database migration helpers:
        'crispy_forms',  # Form layouts
        'avatar',  # for user avatars
    +   'nupages',
    )

# add nupages url namespace to PROJECT_NAME/config/urls.py to the bottom of urlpatterns (lines 13 - 33)

.. code-block:: python

    urlpatterns = patterns('',
        url(r'^$',
            TemplateView.as_view(template_name='pages/home.html'),
            name="home"),
        url(r'^about/$',
            TemplateView.as_view(template_name='pages/about.html'),
            name="about"),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    
        # User management
        url(r'^users/', include("users.urls", namespace="users")),
        url(r'^accounts/', include('allauth.urls')),
    
        # Uncomment the next line to enable avatars
        url(r'^avatar/', include('avatar.urls')),
    
        # Your stuff: custom urls go here
    +    url(r'^pages/', include("nupages.urls", namespace="nupages")),
    
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# sync the database

.. code-block:: bash

    python PROJECT_NAME/manage.py syndb
    python PROJECT_NAME/manage.py migrate
    grunt serve # open 127.0.0.1:8000 in browser


### Production Setup
    
.. code-block:: bash

    heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups
    heroku addons:add sendgrid:starter
    heroku addons:add memcachier:dev
    heroku pg:promote HEROKU_POSTGRESQL_COLOR
    heroku config:set DJANGO_CONFIGURATION=Production
    heroku config:set DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
    heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
    heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
    heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=BUCKET
    git push heroku master
    heroku run python ccx/manage.py syncdb --noinput --settings=config.settings
    heroku run python ccx/manage.py migrate --settings=config.settings
    heroku run python ccx/manage.py collectstatic --settings=config.settings
    
    
