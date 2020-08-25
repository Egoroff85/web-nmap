import nmap

from webnmap.celery import app


@app.task
def get_scan_result(hostname, arguments):
    nm = nmap.PortScanner()
    nm.scan(hosts=hostname, arguments=arguments)
    return nm.csv()