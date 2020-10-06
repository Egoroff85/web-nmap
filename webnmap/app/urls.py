from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('newscan/', NewScan.as_view(), name='new_scan'),
    path('report/<int:id>/', Report.as_view(), name='report'),
    path('report/delete/<int:id>/', DeleteReport.as_view(), name='delete_report'),
]