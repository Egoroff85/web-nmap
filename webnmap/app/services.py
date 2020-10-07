import csv
import io
import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from xhtml2pdf import pisa


class NmapCSVReportParser:
    def __init__(self, nmap_csv_output):
        self.csv_report = io.StringIO(nmap_csv_output)

    def convert_report_to_json(self):
        reader = csv.reader(self.csv_report, delimiter=';')
        next(reader)
        result = {}
        current_hostname = None
        for line in reader:
            ip, hostname, hostname_type, protocol, port, name, state, *_ = line
            if hostname != '':
                if hostname != current_hostname:
                    result[hostname] = []
                    current_hostname = hostname
            else:
                if ip != current_hostname:
                    result[ip] = []
                    current_hostname = ip

            result[current_hostname].append({
                'protocol': protocol,
                'port': port,
                'name': name,
                'state': state
            })
        return result


class ReportExporter:
    def __init__(self, template, scan):
        self.template = template
        self.scan = scan
        self.filetype = None
        self.mime_type = None

    def export(self):
        raise NotImplementedError

    def _create_http_response(self, report):
        filename = f"Report_{self.scan.pk}.{self.filetype}"
        response = HttpResponse(report, content_type=self.mime_type)
        content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response


class PDFReportExporter(ReportExporter):
    def __init__(self, template, scan):
        super().__init__(template, scan)
        self.filetype = 'pdf'
        self.mime_type = 'application/pdf'

    def export(self):
        template = get_template(self.template)
        html = template.render({'scan': self.scan})
        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
        if not pdf.err:
            return self._create_http_response(result.getvalue())
        return None


class HTMLReportExporter(ReportExporter):
    def __init__(self, template, scan):
        super().__init__(template, scan)
        self.filetype = 'html'
        self.mime_type = 'text/html'

    def export(self):
        html = render_to_string(self.template, {'scan': self.scan})
        return self._create_http_response(html)


class JSONReportExporter(ReportExporter):
    def __init__(self, template, scan):
        super().__init__(template, scan)
        self.filetype = 'json'
        self.mime_type = 'application/json'

    def export(self):
        js = json.dumps(self.scan.report, indent=4)
        return self._create_http_response(js)
