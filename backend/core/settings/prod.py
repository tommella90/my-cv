import os
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "tommella-cv-prod-ee14d9b8bb74.herokuapp"]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

REDIS_URL = os.environ["REDIS_URL"]
CELERY_BROKER_URL = REDIS_URL

# if u add caches, remember to add the REDIS_URL to the CACHES dict