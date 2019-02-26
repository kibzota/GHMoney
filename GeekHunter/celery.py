from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeekHunter.settings')
app = Celery('GeekHunter')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.conf.beat_schedule = settings.CELERY_BEAT_SCHEDULE
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
