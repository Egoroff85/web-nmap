import datetime

import nmap

from webnmap.celery import app
from .models import Scan


@app.task
def get_scan_result(scan_id):
    s = Scan.objects.get(pk=scan_id)
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=s.hostname, arguments=s.arguments)
        result = nm.csv()
    except Exception:
        s.status = 'Ошибка'
        s.finished_at = datetime.datetime.now()
        s.is_finished = True
        s.save()
        return
    s.status = 'Завершено'
    s.is_finished = True
    s.report = result
    s.save()
