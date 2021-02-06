from __future__ import absolute_import, unicode_literals

import os
from celery import Celery, shared_task

# Set default Django settings os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yektanet.settings')
app = Celery('yektanet')
# Celery will apply all configuration keys with defined namespace  app.config_from_object('django.conf:settings', namespace='CELERY')
# Load tasks from all registered apps


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#
# @shared_task()
# def test():
#     print("Test")
