from datetime import datetime

from django.shortcuts import render
from user_agents import parse

from main.models import RequestsLog, Versions


def home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Home Page')
        return render(request, 'index.html')
    return render(request, 'index.html')


def intro_page(request):
    if request.method == 'GET':
        send_sms(request, 'Intro Page')
        return render(request, 'intro_script.html')
    return render(request, 'intro_script.html')


def choices_page(request):
    if request.method == 'GET':
        send_sms(request, 'Choices Page')
        return render(request, 'button_index.html')
    return render(request, 'button_index.html')


def blooming_flower_page(request):
    if request.method == 'GET':
        send_sms(request, 'Blooming Flower Page')
        return render(request, 'blooming.html')
    return render(request, 'blooming.html')


def calming_home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Calming Home Page')
        return render(request, 'calming_style.html')
    return render(request, 'calming_style.html')


def solar_system_page(request):
    if request.method == 'GET':
        send_sms(request, 'Solar System Page')
        return render(request, 'universe_index.html')
    return render(request, 'universe_index.html')


def alerting(request):
    if request.method == 'GET':
        send_sms(request, 'Alerting Page')
        return render(request, 'soon_style.html')
    return render(request, 'soon_style.html')


def firefly_page(request):
    if request.method == 'GET':
        send_sms(request, 'Firefly Page')
        return render(request, 'firefly_style.html')
    return render(request, 'firefly_style.html')


def just_home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Just Home Page')
        return render(request, 'home_script.html')
    return render(request, 'home_script.html')


def tree_page(request):
    if request.method == 'GET':
        send_sms(request, 'Tree Page')
        return render(request, 'tree_style.html')
    return render(request, 'tree_style.html')


def congrats_page(request):
    if request.method == 'GET':
        send_sms(request, 'Congrats Page')
        return render(request, 'congrats_style.html')
    return render(request, 'congrats_style.html')


def neon_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Neon Rain Page')
        return render(request, 'neon_style.html')
    return render(request, 'neon_style.html')


def street_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Street Rain Page')
        return render(request, 'rainy_style.html')
    return render(request, 'rainy_style.html')


def simple_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Simple Rain Page')
        return render(request, 'simple_style.html')
    return render(request, 'simple_style.html')


def portal_page(request):
    if request.method == 'GET':
        send_sms(request, 'Portal Page')
        return render(request, 'portal_style.html')
    return render(request, 'portal_style.html')


def bunny_page(request):
    if request.method == 'GET':
        send_sms(request, 'Bunny Page')
        return render(request, 'bunny_style.html')
    return render(request, 'bunny_style.html')


def winter_page(request):
    if request.method == 'GET':
        send_sms(request, 'Winter Page')
        return render(request, 'winter_style.html')
    return render(request, 'winter_style.html')


def summer_page(request):
    if request.method == 'GET':
        send_sms(request, 'Summer Page')
        return render(request, 'summer.html')
    return render(request, 'summer.html')


def musical_lights_page(request):
    if request.method == 'GET':
        send_sms(request, 'Musical Lights Page')
        return render(request, 'musical.html')
    return render(request, 'musical.html')


def cycling(request):
    if request.method == 'GET':
        send_sms(request, 'Cycling Page')
        return render(request, 'biking.html')
    return render(request, 'biking.html')


def seasons(request):
    if request.method == 'GET':
        send_sms(request, 'Seasons Page')
        return render(request, 'seasons.html')
    return render(request, 'seasons.html')


def space_travel(request):
    if request.method == 'GET':
        send_sms(request, 'Space Travel Page')
        return render(request, 'space_travel.html')
    return render(request, 'space_travel.html')


def wild_flowers(request):
    if request.method == 'GET':
        send_sms(request, 'Wild Flower Page')
        return render(request, 'wild_flowers.html')
    return render(request, 'wild_flowers.html')


def flying_bunny(request):
    if request.method == 'GET':
        send_sms(request, 'Flying Bunny Page')
        return render(request, 'flying_bunny.html')
    return render(request, 'flying_bunny.html')


def abstraction(request):
    if request.method == 'GET':
        send_sms(request, 'Abstraction Page')
        return render(request, 'abstraction.html')
    return render(request, 'abstraction.html')


def secret_room(request):
    if request.method == 'GET':
        send_sms(request, 'Secret Page')
        return render(request, 'lock_style.html')
    return render(request, 'lock_style.html')


def statics(request):
    if request.method == 'GET':
        send_sms(request, 'Statics Page')
        
        # Stats page without authentication dependencies
        context = {
            'five_st': 0,
            'four_st': 0,
            'three_st': 0,
            'two_st': 0,
            'one_st': 0,
            'all_rated': 28,
            'not_rated': 28,
        }

        return render(request, 'statics.html', context)
    
    # For non-GET requests, return with empty context
    context = {
        'five_st': 0,
        'four_st': 0,
        'three_st': 0,
        'two_st': 0,
        'one_st': 0,
        'all_rated': 28,
        'not_rated': 28,
    }
    return render(request, 'statics.html', context)


def timeline(request):
    if request.method == 'GET':
        versions = Versions.objects.all()

        context = {'versions': versions}

        send_sms(request, 'Timeline Page')
        return render(request, 'timeline.html', context)
    
    # For non-GET requests, return with empty queryset
    versions = Versions.objects.all()
    context = {'versions': versions}
    return render(request, 'timeline.html', context)




def send_sms(entered_request, in_url):
    # Get the user's IP address
    x_forwarded_for = entered_request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0].strip()
    else:
        ip_address = entered_request.META.get('REMOTE_ADDR')

    # Default to localhost if IP address is not available
    if not ip_address:
        ip_address = '127.0.0.1'

    # Get user agent string and parse it
    user_agent_string = entered_request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)

    current_time = datetime.now()

    RequestsLog.objects.create(
        ip_address=ip_address,
        browser=user_agent.browser.family,
        os=user_agent.os.family,
        device_type=user_agent.device.family,
        is_mobile=user_agent.is_mobile,
        is_tablet=user_agent.is_tablet,
        is_pc=user_agent.is_pc,
        referred_to=in_url,
        request_time=current_time)
