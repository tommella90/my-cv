release: python manage.py migrate
web: gunicorn core.wsgi:application
worker: celery -A core worker --loglevel=info
