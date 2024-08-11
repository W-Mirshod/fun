from django.urls import path
from main.views import HomePage, ChoicesPage, BloomingFlowersPage, CalmingHomePage, SolarSystemPage, OrangePage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('just-choose', ChoicesPage.as_view(), name='choices'),
    path('flower-blooming', BloomingFlowersPage.as_view(), name='blooming'),
    path('calming-view', CalmingHomePage.as_view(), name='calming'),
    path('solar-system', SolarSystemPage.as_view(), name='solar'),
    path('orange', OrangePage.as_view(), name='orange'),
]
