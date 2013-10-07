Static pages with Jinja Templates
=================================

By leveraging flask you can quickly prototype static pages using Jinja
tempaltes. 

Local Development
-----------------

Flask comes equipped with a runserver similar to the one used with Django
allowing quick template development. The Flask app can pass in context
variables to Jinja templates. 

- There is no configuration required for static files.
- There is no settings.py file.

From the command line::

    python controller.py

Deployment
----------

Using frozen_flask allows static pages to be generated essentially by calling
get on each of the pages defined in the app controller.py. So all you have to
do is FTP the static files to an apache/nginx server.

From the command line::
    
    python controller.py build


