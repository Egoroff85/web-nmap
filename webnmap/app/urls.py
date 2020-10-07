from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('newscan/', NewScan.as_view(), name='new_scan'),
    path('report/<int:id>/', Report.as_view(), name='report'),
    path('report/delete/<int:id>/', DeleteReport.as_view(), name='delete_report'),
    path('schedules/', Schedules.as_view(), name='schedules'),
    path('schedules/delete/<int:id>/', DeleteSchedule.as_view(), name='delete_schedule'),
    path('toggle_schedule/', ToggleSchedule.as_view(), name='toggle_schedule'),
    path('export/json/<int:id>/', ExportJSON.as_view(), name='export_json'),
    path('export/html/<int:id>/', ExportHTML.as_view(), name='export_html'),
    path('export/pdf/<int:id>/', ExportPDF.as_view(), name='export_pdf'),
]
