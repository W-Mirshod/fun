from django.urls import path

from main import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('intro/', views.intro_page, name='intro'),
    path('lock/', views.locking_page, name='locking'),
    path('rate/', views.rate_page, name='rate'),
    path('submit_rating', views.submit_rating, name='submit_rating'),
    path('just-choose/', views.choices_page, name='choices'),
    path('flower-blooming/', views.blooming_flower_page, name='blooming'),
    path('calming-view/', views.calming_home_page, name='calming'),
    path('solar-system/', views.solar_system_page, name='solar'),
    path('ratings/', views.ratings_page, name='ratings'),
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
]
