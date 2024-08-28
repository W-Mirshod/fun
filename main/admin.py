from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from main.models import RequestsLog


class RequestsResource(resources.ModelResource):
    class Meta:
        model = RequestsLog
        exclude = ()


@admin.register(RequestsLog)
class RequestsLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RequestsResource
    list_display = ['ip_address', 'request_time', 'device_type', 'referred_to', 'browser', 'os', 'is_mobile',
                    'is_tablet', 'is_pc']
    list_filter = ['request_time', 'ip_address']
    search_fields = ['device_type', 'ip_address']
