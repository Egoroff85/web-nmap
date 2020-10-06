import json

from django.http import HttpResponse
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

            if form.cleaned_data['add_schedule']:
                Schedule.objects.create(
                    hostname=hostname,
                    arguments=arguments,
                    is_active=True,
                    interval=form.cleaned_data['interval']
                )
                return redirect('home')

            s = Scan.objects.create()
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


class Schedules(View):
    def get(self, request):
        schedules = Schedule.objects.all()
        return render(request, 'schedules.html', {'schedules': schedules})


class DeleteSchedule(View):
    def get(self, request, id):
        schedule = Schedule.objects.get(pk=id)
        schedule.delete()
        schedules = Schedule.objects.all()
        return render(request, 'schedules.html', {'schedules': schedules})


class ToggleSchedule(View):
    def post(self, request):
        if request.is_ajax():
            try:
                data = json.loads(request.body)
                schedule = Schedule.objects.get(pk=data['id'])
                schedule.is_active = data['is_active']
                schedule.save()
                resp = {'status': 'ok',
                        'is_active': schedule.is_active}
            except Exception:
                resp = {'status': 'error'}
            return HttpResponse(json.dumps(resp), content_type='application/json')
