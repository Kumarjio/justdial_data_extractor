import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justdial_main.settings')

app = Celery('justdial_main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()