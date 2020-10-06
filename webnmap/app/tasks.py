import datetime

import nmap

from webnmap.celery import celery_app
from .models import *

from .services import NmapCSVReportParser


@celery_app.task
def get_scan_result(scan_id):
    s = Scan.objects.get(pk=scan_id)
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=s.hostname.hostname, arguments=s.arguments.arguments)
        result = nm.csv()
    except Exception:
        s.status = 'Ошибка'
        s.finished_at = datetime.datetime.now()
        s.is_finished = True
        s.save()
        return

    s.status = 'Завершено'
    s.is_finished = True
    p = NmapCSVReportParser(result)
    report = p.convert_report_to_json()
    s.report = report
    s.save()


@celery_app.task
def schedule_scan(interval):
    scan_schedules = Schedule.objects.filter(interval=interval, is_active=True)
    for scan_schedule in scan_schedules:
        s = Scan.objects.create(hostname=scan_schedule.hostname, arguments=scan_schedule.arguments)
        get_scan_result.apply_async(args=[s.pk])