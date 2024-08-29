import os
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)

# ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "tommella-cv-prod-ee14d9b8bb74.herokuapp"]
ALLOWED_HOSTS = ['tommella-cv-prod-ee14d9b8bb74.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}
print(DATABASES)

REDIS_URL = os.environ["REDIS_URL"]
CELERY_BROKER_URL = REDIS_URL

# if u add caches, remember to add the REDIS_URL to the CACHES dict