from datetime import datetime

import requests
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from user_agents import parse

from root import settings


def home_page(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def choices_page(request):
    if request.method == 'GET':
        send_sms(request)
        return render(request, 'button_index.html')


def blooming_flower_page(request):
    if request.method == 'GET':
        return render(request, 'blooming.html')


def calming_home_page(request):
    if request.method == 'GET':
        return render(request, 'calming_style.html')


def solar_system_page(request):
    if request.method == 'GET':
        return render(request, 'universe_index.html')


def intro_page(request):
    if request.method == 'GET':
        return render(request, 'intro_style.html')


def alerting(request):
    if request.method == 'GET':
        request.session['popup_message'] = \
            "You currently can not enter this page. Sorry but it is not fully done yet, Orange !"
        popup_message = request.session.pop('popup_message', None)
        if not popup_message:
            redirect('choices')
        context = {'popup_message': popup_message}

        return render(request, 'alert.html', context)


def firefly_page(request):
    if request.method == 'GET':
        return render(request, 'firefly_style.html')


def just_home_page(request):
    if request.method == 'GET':
        return render(request, 'home_script.html')


def tree_page(request):
    if request.method == 'GET':
        return render(request, 'tree_style.html')


def congrats_page(request):
    if request.method == 'GET':
        return render(request, 'congrats_style.html')


def neon_rain_page(request):
    if request.method == 'GET':
        return render(request, 'neon_style.html')


def street_rain_page(request):
    if request.method == 'GET':
        return render(request, 'rainy_style.html')


def simple_rain_page(request):
    if request.method == 'GET':
        return render(request, 'simple_style.html')


def portal_page(request):
    if request.method == 'GET':
        return render(request, 'portal_style.html')


def bunny_page(request):
    if request.method == 'GET':
        return render(request, 'bunny_style.html')


def send_sms(entered_request):
    # Get the user's IP address
    x_forwarded_for = entered_request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]  # Use the first IP in the list
    else:
        ip_address = entered_request.META.get('REMOTE_ADDR')

    # Get user agent string and parse it
    user_agent_string = entered_request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_string)

    # Additional META information
    referer = entered_request.META.get('HTTP_REFERER', 'No Referrer')
    accept_language = entered_request.META.get('HTTP_ACCEPT_LANGUAGE', 'No Language Info')
    host = entered_request.META.get('HTTP_HOST', 'No Host Info')

    # Get location data based on IP
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        location_data = response.json()
        city = location_data.get('city')
        country = location_data.get('country_name')
    except requests.RequestException as e:
        city = 'Unknown'
        country = 'Unknown'

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create the email message
    subject = "Request to Website"
    message = (
        f"IP Address: {ip_address}\n"
        f"City: {city}\n"
        f"Country: {country}\n\n"
        f"User Agent: {user_agent_string}\n"
        f"Browser: {user_agent.browser.family}\n"
        f"OS: {user_agent.os.family}\n"
        f"Device Type: {user_agent.device.family}\n"
        f"Is Mobile: {user_agent.is_mobile}\n"
        f"Is Tablet: {user_agent.is_tablet}\n"
        f"Is PC: {user_agent.is_pc}\n\n"
        f"Referrer: {referer}\n"
        f"Accept Language: {accept_language}\n"
        f"Host: {host}\n\n"
        f"Request Time: {current_time}"
    )

    # Send the email
    recipient_list = ['trading3526@gmail.com']
    send_mail(subject,
              message,
              settings.DEFAULT_FROM_EMAIL,
              recipient_list,
              fail_silently=False)

# class HomePage(View):
#     def get(self, request):
#         return render(request, 'index.html')


# class ChoicesPage(View):
#     def get(self, request):
#         return render(request, 'button_index.html')


# class BloomingFlowersPage(View):
#     def get(self, request):
#         return render(request, 'blooming.html')


# class CalmingHomePage(View):
#     def get(self, request):
#         return render(request, 'calming_style.html')


# class SolarSystemPage(View):
#     def get(self, request):
#         return render(request, 'universe_index.html')


# class OrangePage(View):
#     def get(self, request):
#         return render(request, 'orange_style.html')


# class FireFlyPage(View):
#     def get(self, request):
#         return render(request, 'firefly_style.html')


# class JustHomePage(View):
#     def get(self, request):
#         return render(request, 'home_script.html')


# class TreePage(View):
#     def get(self, request):
#         return render(request, 'tree_style.html')
