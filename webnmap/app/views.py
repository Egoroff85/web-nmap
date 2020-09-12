from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Scan
from .tasks import get_scan_result


class IndexView(View):
    def get(self, request):
        if not request.is_ajax():
            scans = Scan.objects.all()
            return render(request, 'index.html', {'scans': scans})

        # books = list(Book.objects.values())
        # return HttpResponse(json.dumps(books), content_type='application/json')


class NewScan(View):
    def get(self, request):
        if not request.is_ajax():
            return render(request, 'newscan.html')

    def post(self, request):
        s = Scan(hostname=request.POST['host'], arguments=request.POST['arguments'])
        s.save()
        get_scan_result.apply_async(args=[s.pk])
        # get_scan_result.delay(s.pk)
        return redirect('home')


class Report(View):
    def get(self, request, id):
        scan = Scan.objects.get(pk=id)
        return render(request, 'report.html', {'scan': scan})