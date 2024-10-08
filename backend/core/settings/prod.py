import os
from .common import *
import dj_database_url
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

# Now you can access the SECRET_KEY from the environment
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

# ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]
ALLOWED_HOSTS = ['tommella-cv-prod-ee14d9b8bb74.herokuapp.com', ]


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

# SECURE_CROSS_ORIGIN_OPENER_POLICY = None

# REDIS_URL = os.environ["REDIS_URL"]
# CELERY_BROKER_URL = REDIS_URL

# if u add caches, remember to add the REDIS_URL to the CACHES dict