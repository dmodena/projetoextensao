from projetoextensao.settings.base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['projetoextensao.herokuapp.com']
SECRET_KEY = os.environ['DJANGO_KEY']
DATABASES['default'] = dj_database_url.config()
