from django.shortcuts import render
from django.views.generic import View
import nmap


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        hostname = request.POST['host']
        arguments = request.POST['arguments']
        nm = nmap.PortScanner()
        nm.scan(hosts=hostname, arguments=arguments)
        context = {
            'results': nm.csv()
        }
        return render(request, 'results.html', context)
