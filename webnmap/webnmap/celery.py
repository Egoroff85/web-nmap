import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webnmap.settings")

celery_app = Celery("webnmap")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from app.tasks import schedule_scan

    sender.add_periodic_task(
        crontab(hour='*/1'),
        schedule_scan.s(1),
    )
    sender.add_periodic_task(
        crontab(hour='*/2'),
        schedule_scan.s(2),
    )
    sender.add_periodic_task(
        crontab(hour='*/4'),
        schedule_scan.s(4),
    )
    sender.add_periodic_task(
        crontab(hour='*/8'),
        schedule_scan.s(8),
    )
