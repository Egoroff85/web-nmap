import nmap


def get_result_csv(hostname, arguments):
    nm = nmap.PortScanner()
    nm.scan(hosts=hostname, arguments=arguments)
    return nm.csv()
