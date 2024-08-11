from django.urls import path
from main.views import HomeView, ChoicesPage, BloomingFlowersPage

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('just-choose', ChoicesPage.as_view(), name='choices'),
    path('flower-blooming', BloomingFlowersPage.as_view(), name='blooming'),
]
