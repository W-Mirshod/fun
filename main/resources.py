from import_export import resources

from main.models import RequestsLog, Intro, Versions, CustomUser, Contacting, Rates


class CustomUsersResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RequestsResource(resources.ModelResource):
    class Meta:
        model = RequestsLog
        fields = '__all__'


class IntroResource(resources.ModelResource):
    class Meta:
        model = Intro
        fields = ['id', 'title', 'slug', 'description', 'image', 'created_at']


class RatesResource(resources.ModelResource):
    class Meta:
        model = Rates
        fields = '__all__'


class VersionsResource(resources.ModelResource):
    class Meta:
        model = Versions
        fields = ['id', 'versions', 'description', 'created_at', 'updated_at']


class ContactingResource(resources.ModelResource):
    class Meta:
        model = Contacting
        fields = '__all__'
