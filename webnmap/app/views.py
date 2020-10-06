from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import NewScanForm
from .models import *
from .tasks import get_scan_result

from celery.task.control import revoke


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
            form = NewScanForm()
            return render(request, 'newscan.html', {'form': form})

    def post(self, request):
        form = NewScanForm(request.POST)
        if form.is_valid():
            hostname, _ = Hostname.objects.get_or_create(hostname=form.cleaned_data['hostname'].strip())
            arguments, _ = Arguments.objects.get_or_create(arguments=form.cleaned_data['arguments'])
            s = Scan.objects.create(hostname=hostname, arguments=arguments)
            uuid = get_scan_result.apply_async(args=[s.pk])
            s.celery_task_id = uuid
            s.save()
            return redirect('home')
        else:
            return render(request, 'newscan.html', {'form': form})


class Report(View):
    def get(self, request, id):
        scan = Scan.objects.get(pk=id)
        return render(request, 'report.html', {'scan': scan})


class DeleteReport(View):
    def get(self, request, id):
        scan = Scan.objects.get(pk=id)
        if scan.status == 'В процессе':
            revoke(task_id=scan.celery_task_id, terminate=True)
        scan.delete()

        scans = Scan.objects.all()
        return render(request, 'index.html', {'scans': scans})