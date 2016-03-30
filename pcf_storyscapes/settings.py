# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import json
from urlparse import urlparse
import geonode
from geonode.settings import *

#
# General Django development settings
#

SITENAME = 'pcf_storyscapes'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
GEONODE_ROOT = os.path.abspath(os.path.abspath(geonode.__file__))
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WSGI_APPLICATION = "pcf_storyscapes.wsgi.application"


# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'pcf_storyscapes.urls'

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

if 'DEBUG' in os.environ:
	  DEBUG = os.environ.get('DEBUG')

if 'SECRET_KEY' in os.environ:
	  SECRET_KEY = os.environ.get('SECRET_KEY')

if 'DATABASE_URL' and 'POSTGIS_URL' in os.environ:
    import dj_database_url
    POSTGIS = os.environ.get('POSTGIS_URL')
    DATABASES = {'default': dj_database_url.config(conn_max_age=500), 'datastore': dj_database_url.config(POSTGIS, conn_max_age=500)}

if 'GS_URL' and 'GS_USER' and 'GS_PASSWORD' in os.environ:
	  GS_URL = os.environ.get('GS_URL')
    OGC_SERVER = {
        'default' : {
            'BACKEND' : 'geonode.geoserver',
            'LOCATION' : GS_URL,
            'PUBLIC_LOCATION' : GS_URL,
            'USER' : os.environ.get('GS_USER'),
            'PASSWORD' : os.environ.get('GS_PASSWORD'),
            'MAPFISH_PRINT_ENABLED' : True,
            'PRINT_NG_ENABLED' : True,
            'GEONODE_SECURITY_ENABLED' : True,
            'GEOGIG_ENABLED' : True,
            'WMST_ENABLED' : False,
            'DATASTORE': 'datastore',
            'GEOGIG_DATASTORE_DIR':'/var/lib/geoserver_data/geogig',
        }
    }

if 'ES_URL' in os.environ:
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': os.environ.get('ES_URL'),
            'INDEX_NAME': os.environ.get('ES_INDEX', 'storyscapes'),
            },
    }
    INSTALLED_APPS += (
        'haystack',
    )

if 'RABBITMQ_URL' in os.environ:
	  BROKER_URL = os.environ.get('RABBITMQ_URL')
    CELERY_ALWAYS_EAGER = False
    NOTIFICATION_QUEUE_ALL = not CELERY_ALWAYS_EAGER
