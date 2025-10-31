from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

from main.models import RequestsLog, Intro, Versions
from main.resources import IntroResource, RequestsResource, VersionsResource

admin.site.unregister(Group)


@admin.register(Intro)
class IntroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = IntroResource

    fields = ['title', 'description', 'image']
    list_display = ['__str__', 'title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']
    list_display_links = ['__str__']
    list_editable = ['title', 'description']


@admin.register(RequestsLog)
class RequestsLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RequestsResource

    list_display = ['__str__', 'referred_to', 'request_time', 'device_type', 'browser', 'os', 'is_mobile',
                    'is_tablet', 'is_pc']
    list_filter = ['request_time', 'ip_address']
    search_fields = ['device_type', 'ip_address']


@admin.register(Versions)
class VersionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VersionsResource

    list_display = ['version', 'description', 'created_at']
    list_filter = ['version', 'created_at']
    search_fields = ['version']
