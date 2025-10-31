from import_export import resources

from main.models import RequestsLog, Intro, Versions


class RequestsResource(resources.ModelResource):
    class Meta:
        model = RequestsLog
        fields = '__all__'


class IntroResource(resources.ModelResource):
    class Meta:
        model = Intro
        fields = ('id', 'title', 'slug', 'description', 'image', 'created_at')


class VersionsResource(resources.ModelResource):
    class Meta:
        model = Versions
        fields = ('id', 'version', 'description', 'created_at', 'updated_at')
