from django.urls import path
from main.views import MainPage, BloomingFlowersPage

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('flower-blooming', BloomingFlowersPage.as_view(), name='blooming'),
]
