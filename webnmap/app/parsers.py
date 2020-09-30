import csv
import io


class NmapCSVReportParser():
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
                    result[hostname] = {}
                    current_hostname = hostname
            else:
                if ip != current_hostname:
                    result[ip] = {}
                    current_hostname = ip

            key = f'{protocol}_{port}'
            result[current_hostname][key] = {
                'protocol': protocol,
                'port': port,
                'name': name,
                'state': state
            }
        return result

# {
#     'hostname or ip': {
#         'protocol_port': {
#             'protocol': 'protocol',
#             'port': 'port',
#             'name': 'name',
#             'state': 'state'
#         }
#     }
# }
