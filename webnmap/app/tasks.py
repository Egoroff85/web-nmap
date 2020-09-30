import datetime

import nmap

from webnmap.celery import app
from .models import *

from .parsers import NmapCSVReportParser

@app.task
def get_scan_result(scan_id):
    s = Scan.objects.get(pk=scan_id)
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=s.hostname.hostname, arguments=s.arguments.arguments)
        result = nm.csv()
    except Exception:
        try:
            status = Status.objects.get(status='Ошибка')
        except Exception:
            status = Status(status='Ошибка')
            status.save()
        s.status = status
        s.finished_at = datetime.datetime.now()
        s.is_finished = True
        s.save()
        return
    try:
        status = Status.objects.get(status='Завершено')
    except Exception:
        status = Status(status='Завершено')
        status.save()
    s.status = status
    s.is_finished = True
    p = NmapCSVReportParser(result)
    report = p.convert_report_to_json()
    s.report = report
    s.save()
