from django.contrib import admin

from .models import Scan


class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'started_at', 'hostname', 'arguments', 'finished_at', 'status')
    list_display_links = ('id', 'hostname', 'arguments')
    search_fields = ('hostname', 'arguments')


admin.site.register(Scan, ScanAdmin)

