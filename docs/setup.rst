=============
Setup
=============


add 'nupages' to project settings.py in INSTALLED_APPS

.. code-block:: python

	INSTALLED_APPS = (
	...
	'nupages',
    )

add 'nupages.middleware.MultiTenantMiddleware' to project settings.py in MIDDLEWARE_CLASSES if you want the multi-tenant support

.. code-block:: python

    MIDDLEWARE_CLASSES = (
    ...
    'nupages.middleware.MultiTenantMiddleware',
    )

add nupages url namespace to project urls.py, you can replace `pages/` with whatever

.. code-block:: python

    urlpatterns = patterns('',
    ...
    url(r'^pages/', include("nupages.urls", namespace="nupages")), 
    )

sync the database

.. code-block:: bash

    python PROJECT_NAME/manage.py syndb
    python PROJECT_NAME/manage.py migrate