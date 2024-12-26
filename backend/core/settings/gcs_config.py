import os
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
from django.core.files.storage import default_storage


GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'secrets/tommella-website-283affeff4f2.json')
)

GS_BUCKET_NAME = 'tommella-website-storage'
