from django.urls import path
from main.views import HomePage, ChoicesPage, BloomingFlowersPage, CalmingHomePage, SolarSystemPage, orange_page, \
    FireFlyPage, JustHomePage, TreePage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('just-choose', ChoicesPage.as_view(), name='choices'),
    path('flower-blooming', BloomingFlowersPage.as_view(), name='blooming'),
    path('calming-view', CalmingHomePage.as_view(), name='calming'),
    path('solar-system', SolarSystemPage.as_view(), name='solar'),
    path('orange', orange_page, name='orange'),
    path('firefly/', FireFlyPage.as_view(), name='firefly'),
    path('just-house/', JustHomePage.as_view(), name='just_home'),
    path('tree/', TreePage.as_view(), name='tree'),
]
