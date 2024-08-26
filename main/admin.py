from django.contrib import admin

from main.models import RequestsLog


@admin.register(RequestsLog)
class RequestsLogAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'request_time', 'device_type', 'referred_to', 'browser', 'os', 'is_mobile',
                    'is_tablet', 'is_pc']
    list_filter = ['request_time', 'ip_address']
    search_fields = ['device_type', 'ip_address']
