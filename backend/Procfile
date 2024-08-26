release: python manage.py migrate
web: gunicorn core.wsgi
worker: celery -a core.worker