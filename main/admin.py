from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from main.models import RequestsLog, Ratings, Rates, CustomUser

admin.site.register(CustomUser)


class RequestsResource(resources.ModelResource):
    class Meta:
        model = RequestsLog
        fields = '__all__'


class RatingsResource(resources.ModelResource):
    class Meta:
        model = Ratings
        fields = '__all__'


@admin.register(RequestsLog)
class RequestsLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RequestsResource
    list_display = ['ip_address', 'request_time', 'device_type', 'referred_to', 'browser', 'os', 'is_mobile',
                    'is_tablet', 'is_pc']
    list_filter = ['request_time', 'ip_address']
    search_fields = ['device_type', 'ip_address']


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    resource_class = RatingsResource

    list_display = ['title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ['rate', 'updated_at', 'created_at']
    list_filter = ['rate', 'updated_at']
