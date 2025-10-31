from django.urls import path, re_path
from django.shortcuts import redirect

import main.views.pages as views

def auth_redirect(request):
    """Redirect old auth URLs to home since authentication is no longer required"""
    return redirect('/')

urlpatterns = [
    # pages
    path('', views.home_page, name='index'),
    # Handle old auth URLs - redirect to home
    re_path(r'^auth/.*', auth_redirect),
    path('intro/', views.intro_page, name='intro'),
    path('just-choose/', views.choices_page, name='choices'),
    path('flower-blooming/', views.blooming_flower_page, name='blooming'),
    path('calming-view/', views.calming_home_page, name='calming'),
    path('solar-system/', views.solar_system_page, name='solar'),
    path('firefly/', views.firefly_page, name='firefly'),
    path('just-house/', views.just_home_page, name='just_home'),
    path('tree/', views.tree_page, name='tree'),
    path('animation/', views.alerting, name='alerting'),
    path('congrats/', views.congrats_page, name='congrats'),
    path('simp-rain/', views.simple_rain_page, name='simp_rain'),
    path('neon-rain/', views.neon_rain_page, name='neon_rain'),
    path('rainy/', views.street_rain_page, name='rainy'),
    path('portal/', views.portal_page, name='portal'),
    path('bunny/', views.bunny_page, name='bunny'),
    path('simple-winter/', views.winter_page, name='winter'),
    path('summer/', views.summer_page, name='summer'),
    path('musical-lights/', views.musical_lights_page, name='musical_lights'),
    path('cycling/', views.cycling, name='cycling'),
    path('seasons/', views.seasons, name='seasons'),
    path('space-travel/', views.space_travel, name='space_travel'),
    path('wild-flowers/', views.wild_flowers, name='wild_flowers'),
    path('flying-bunny/', views.flying_bunny, name='flying_bunny'),
    path('abstraction/', views.abstraction, name='abstraction'),
    path('timeline/', views.timeline, name='timeline'),
    path('statics/', views.statics, name='statics'),
    path('secret-room/', views.secret_room, name='secret_room'),
]
