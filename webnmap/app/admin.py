from django.contrib import admin

from .models import *


class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'started_at', 'hostname', 'arguments', 'finished_at', 'status')
    list_display_links = ('id', 'hostname', 'arguments')
    search_fields = ('hostname', 'arguments')


class HostnameAdmin(admin.ModelAdmin):
    list_display = ('hostname',)
    list_display_links = ('hostname',)
    search_fields = ('hostname',)


class ArgumentsAdmin(admin.ModelAdmin):
    list_display = ('arguments',)
    list_display_links = ('arguments',)
    search_fields = ('arguments',)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'interval', 'is_active', 'hostname', 'arguments')
    list_display_links = ('id', 'interval', 'hostname', 'arguments')
    search_fields = ('interval', 'hostname', 'arguments')
    list_editable = ('is_active',)
    list_filter = ('is_active',)


admin.site.register(Scan, ScanAdmin)
admin.site.register(Hostname, HostnameAdmin)
admin.site.register(Arguments, ArgumentsAdmin)
admin.site.register(Schedule, ScheduleAdmin)
