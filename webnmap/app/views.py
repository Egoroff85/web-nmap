from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import NewScanForm
from .models import *
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
            form = NewScanForm()
            return render(request, 'newscan.html', {'form': form})

    def post(self, request):
        form = NewScanForm(request.POST)
        if form.is_valid():
            try:
                status = Status.objects.get(status='В процессе')
            except Exception:
                status = Status()
                status.save()

            try:
                hostname = Hostname.objects.get(hostname=form.cleaned_data['hostname'])
            except Exception:
                hostname = Hostname(hostname=form.cleaned_data['hostname'])
                hostname.save()

            args = form.cleaned_data['arguments'].strip() if form.cleaned_data['arguments'].strip() != '' else '-'
            try:
                arguments = Arguments.objects.get(arguments=args)
            except Exception:
                arguments = Arguments(arguments=args)
                arguments.save()

            s = Scan(hostname=hostname, arguments=arguments, status=status)
            s.save()

            get_scan_result.apply_async(args=[s.pk])
            return redirect('home')
        else:
            return render(request, 'newscan.html', {'form': form})


class Report(View):
    def get(self, request, id):
        scan = Scan.objects.get(pk=id)
        return render(request, 'report.html', {'scan': scan})