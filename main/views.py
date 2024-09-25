from datetime import datetime

from django.shortcuts import render
from user_agents import parse

from main.models import RequestsLog, Ratings


def home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Home Page')
        return render(request, 'index.html')


def locking_page(request):
    if request.method == 'GET':
        send_sms(request, 'Locking Page')
        return render(request, 'lock_style.html')


def rate_page(request):
    if request.method == 'GET':
        send_sms(request, 'Rate Page')
        return render(request, 'rate_style.html')


def intro_page(request):
    if request.method == 'GET':
        send_sms(request, 'Intro Page')
        return render(request, 'intro_script.html')


def choices_page(request):
    if request.method == 'GET':
        send_sms(request, 'Choices Page')
        return render(request, 'button_index.html')


def blooming_flower_page(request):
    if request.method == 'GET':
        send_sms(request, 'Blooming Flower Page')
        return render(request, 'blooming.html')


def calming_home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Calming Home Page')
        return render(request, 'calming_style.html')


def solar_system_page(request):
    if request.method == 'GET':
        send_sms(request, 'Solar System Page')
        return render(request, 'universe_index.html')


def ratings_page(request):
    ratings = Ratings.objects.all()

    if request.method == 'GET':
        send_sms(request, 'Ratings Page')

        context = {'ratings': ratings}
        return render(request, 'ratings_style.html', context)


def alerting(request):
    if request.method == 'GET':
        send_sms(request, 'Alerting Page')

        # request.session['popup_message'] = \
        #     "You currently can not enter this page. Sorry but it is not fully done yet, Orange !"
        # popup_message = request.session.pop('popup_message', None)
        # if not popup_message:
        #     redirect('choices')
        # context = {'popup_message': popup_message}

        return render(request, 'soon_style.html')


def firefly_page(request):
    if request.method == 'GET':
        send_sms(request, 'Firefly Page')
        return render(request, 'firefly_style.html')


def just_home_page(request):
    if request.method == 'GET':
        send_sms(request, 'Just Home Page')
        return render(request, 'home_script.html')


def tree_page(request):
    if request.method == 'GET':
        send_sms(request, 'Tree Page')
        return render(request, 'tree_style.html')


def congrats_page(request):
    if request.method == 'GET':
        send_sms(request, 'Congrats Page')
        return render(request, 'congrats_style.html')


def neon_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Neon Rain Page')
        return render(request, 'neon_style.html')


def street_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Street Rain Page')
        return render(request, 'rainy_style.html')


def simple_rain_page(request):
    if request.method == 'GET':
        send_sms(request, 'Simple Rain Page')
        return render(request, 'simple_style.html')


def portal_page(request):
    if request.method == 'GET':
        send_sms(request, 'Portal Page')
        return render(request, 'portal_style.html')


def bunny_page(request):
    if request.method == 'GET':
        send_sms(request, 'Bunny Page')
        return render(request, 'bunny_style.html')


def winter_page(request):
    if request.method == 'GET':
        send_sms(request, 'Winter Page')
        return render(request, 'winter_style.html')


def submit_rating(request):
    if request.method == 'GET':
        send_sms(request, 'Submit Rating Page')
        return render(request, 'rate_style.html')

    if request.method == 'POST':
        rating = request.POST['rating']
        rating_obj = Ratings(rating=rating)
        rating_obj.save()

        return render(request, 'rate_style.html')


def send_sms(entered_request, in_url):
    # Get the user's IP address
    x_forwarded_for = entered_request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = entered_request.META.get('REMOTE_ADDR')

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
