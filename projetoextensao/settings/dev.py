from projetoextensao.settings.base import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = config('SECRET_KEY')

# Base url for static files
STATIC_FILES_URL = config('STATIC_FILES_URL')
