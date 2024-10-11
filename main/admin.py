from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from main.models import RequestsLog, Intro, Rates, Versions, Contacting, CustomUser
from main.resources import IntroResource, RequestsResource, VersionsResource


@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    resource_class = IntroResource

    list_display = ['title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ['rating', 'rate', 'updated_at', 'created_at']
    list_filter = ['rate', 'updated_at']


@admin.register(RequestsLog)
class RequestsLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RequestsResource

    list_display = ['__str__', 'referred_to', 'request_time', 'device_type', 'browser', 'os', 'is_mobile',
                    'is_tablet', 'is_pc']
    list_filter = ['request_time', 'ip_address']
    search_fields = ['device_type', 'ip_address']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_superuser', 'is_active', 'last_login']
    list_filter = ['username', 'is_active']
    search_fields = ['username']


@admin.register(Versions)
class VersionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VersionsResource

    list_display = ['version', 'description', 'created_at']
    list_filter = ['version', 'created_at']
    search_fields = ['version']


@admin.register(Contacting)
class ContactingAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['user__username']
