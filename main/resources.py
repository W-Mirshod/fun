from import_export import resources

from main.models import RequestsLog, Intro, Versions


class RequestsResource(resources.ModelResource):
    class Meta:
        model = RequestsLog
        fields = '__all__'


class IntroResource(resources.ModelResource):
    class Meta:
        model = Intro
        fields = '__all__'


class VersionsResource(resources.ModelResource):
    class Meta:
        model = Versions
        fields = '__all__'
