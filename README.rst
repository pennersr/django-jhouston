===============
django-jhouston
===============

"Houston, we have a Javascript problem!"

`jhouston` catches Javascript errors occuring in the browser and
automatically posts them to the server. There they are stored in the
database for debugging & analysis purposes. This opens up a whole new
view on what is happening client-side.

Installation
============

settings.py::

    INSTALLED_APPS = (
        ...
        'jhouston',

urls.py::

    urlpatterns = patterns('',
        ...
        (r'^jhouston/', include('jhouston.urls')))

base.html::

    ...
    <script src="/static/jhouston/js/jhouston.js" type="text/javascript">
    </script>

