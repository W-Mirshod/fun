from django.urls import path

from main.views import (home_page, choices_page, blooming_flower_page, calming_home_page, solar_system_page,
                        intro_page, just_home_page, tree_page, alerting, firefly_page, congrats_page)

urlpatterns = [
    path('', home_page, name='index'),
    path('just-choose/', choices_page, name='choices'),
    path('flower-blooming/', blooming_flower_page, name='blooming'),
    path('calming-view/', calming_home_page, name='calming'),
    path('solar-system/', solar_system_page, name='solar'),
    path('intro/', intro_page, name='intro'),
    path('firefly/', firefly_page, name='firefly'),
    path('just-house/', just_home_page, name='just_home'),
    path('tree/', tree_page, name='tree'),
    path('animation/', alerting, name='alerting'),
    path('congrats/', congrats_page, name='congrats'),
]
