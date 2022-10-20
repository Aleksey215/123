import os
from celery import Celery

# для связи настроек Django с настройками Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('ads')  # возможно надо поменять на Game_Site
# чтобы Celery сам находил все необходимые настройки в файле settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')
# для автоматического поиска заданий в файлах tasks.py
app.autodiscover_tasks()
