"""
WSGI config for djcctest project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior djcctest directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

#following added by MB bexcause of path issues on linux server. may be unnecessary
sys.path.append(str(ROOT_DIR / "djcctest"))
sys.path.append(str(ROOT_DIR / "djcctest" / "venv" / "bin" ))

# preparing environment for django settings files
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ["READ_DOT_ENV_FILE"] = True



# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
