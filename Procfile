release: python backend/manage.py migrate
web: gunicorn backend.core.wsgi:application
worker: celery -A backend.core worker --loglevel=info
