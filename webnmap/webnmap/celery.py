import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webnmap.settings")

app = Celery("webnmap")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
