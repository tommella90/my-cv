from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3vz=n^dqr_k)(jj_3l-61@#d9u!dstkoz(675jj^%pnx&u3n5m"

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']
DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "https://tommella90.github.io",
] 
 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'my_cv',
#         'USER': 'tommella90',
#         'PASSWORD': 'ge181090',
#         'HOST': 'localhost',  # or your database host
#         'PORT': '5432',  # default PostgreSQL port
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
