from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from user_agents import parse

from main.forms import ContactingForm
from main.models import RequestsLog, Intro, Rates, Contacting, Versions
from root.settings import DEFAULT_FROM_EMAIL


def home_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Home Page')
        return render(request, 'index.html')


def locking_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Locking Page')
        return render(request, 'lock_style.html')


def rate_page(request, slug):
    if request.method == 'GET':

        save_time_spent(request)
        send_sms(request, 'Rate Page')

        word = None

        rate_number = request.GET.get('rating')
        rating = get_object_or_404(Intro, slug=slug)
        rate = Rates.objects.filter(rating=rating)
        if rate:
            rate = get_object_or_404(Rates, rating=rating)
            if rate.rate:
                if rate.rate == '1':
                    word = 'Terrible'
                elif rate.rate == '2':
                    word = 'Bad'
                elif rate.rate == '3':
                    word = 'Okay'
                elif rate.rate == '4':
                    word = 'Good'
                elif rate.rate == '5':
                    word = 'Perfect'

        if not rate and rate_number:
            rate = Rates.objects.create(rate=rate_number, rating=rating)

        context = {'rate': rate,
                   'word': word, }

        return render(request, 'rate_style.html', context)


def intro_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Intro Page')
        return render(request, 'intro_script.html')


def choices_page(request):
    if request.method == 'GET':
        send_sms(request, 'Choices Page')
        return render(request, 'button_index.html')


def blooming_flower_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Blooming Flower Page')
        return render(request, 'blooming.html')


def calming_home_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Calming Home Page')
        return render(request, 'calming_style.html')


def solar_system_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Solar System Page')
        return render(request, 'universe_index.html')


def ratings_page(request):
    if request.method == 'GET':
        ratings = Intro.objects.all()

        send_sms(request, 'Ratings Page')
        save_time_spent(request)

        context = {'ratings': ratings}
        return render(request, 'ratings_style.html', context)


def alerting(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Alerting Page')

        return render(request, 'soon_style.html')


def firefly_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Firefly Page')
        return render(request, 'firefly_style.html')


def just_home_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Just Home Page')
        return render(request, 'home_script.html')


def tree_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Tree Page')
        return render(request, 'tree_style.html')


def congrats_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Congrats Page')
        return render(request, 'congrats_style.html')


def neon_rain_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Neon Rain Page')
        return render(request, 'neon_style.html')


def street_rain_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Street Rain Page')
        return render(request, 'rainy_style.html')


def simple_rain_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Simple Rain Page')
        return render(request, 'simple_style.html')


def portal_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Portal Page')
        return render(request, 'portal_style.html')


def bunny_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Bunny Page')
        return render(request, 'bunny_style.html')


def winter_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Winter Page')
        return render(request, 'winter_style.html')


def summer_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Summer Page')
        return render(request, 'summer.html')


def musical_lights_page(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Musical Lights Page')
        return render(request, 'musical.html')


def cycling(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Cycling Page')
        return render(request, 'biking.html')


def seasons(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Seasons Page')
        return render(request, 'seasons.html')


def space_travel(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Space Travel Page')
        return render(request, 'space_travel.html')


def wild_flowers(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Wild Flower Page')
        return render(request, 'wild_flowers.html')


def flying_bunny(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Flying Bunny Page')
        return render(request, 'flying_bunny.html')


def abstraction(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Abstraction Page')
        return render(request, 'abstraction.html')


def statics(request):
    if request.method == 'GET':
        five_st = Rates.objects.filter(rate=5).count()
        four_st = Rates.objects.filter(rate=4).count()
        three_st = Rates.objects.filter(rate=3).count()
        two_st = Rates.objects.filter(rate=2).count()
        one_st = Rates.objects.filter(rate=1).count()

        all_rated = 21
        not_rated = all_rated - (five_st + four_st + three_st + two_st + one_st)

        save_time_spent(request)
        send_sms(request, 'Statics Page')

        context = {'five_st': five_st,
                   'four_st': four_st,
                   'three_st': three_st,
                   'two_st': two_st,
                   'one_st': one_st,
                   'all_rated': all_rated,
                   'not_rated': not_rated, }

        return render(request, 'statics.html', context)


def timeline(request):
    if request.method == 'GET':
        save_time_spent(request)
        versions = Versions.objects.all()

        context = {'versions': versions}

        send_sms(request, 'Timeline Page')
        return render(request, 'timeline.html', context)


def submit_rating(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Submit Rating Page')
        return render(request, 'rate_style.html')

    if request.method == 'POST':
        rating = request.POST['rating']
        rating_obj = Intro(rating=rating)
        rating_obj.save()

        return render(request, 'rate_style.html')


def contacting(request):
    if request.method == 'GET':
        save_time_spent(request)
        send_sms(request, 'Contacting Page')
        form = ContactingForm(request.GET)

        return render(request, 'contacting.html', {'form': form})
    if request.method == 'POST':
        form = ContactingForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                Contacting.objects.create(user=request.user, body=form.cleaned_data['body'])

                request.session['messages'] = "Thanks for your contribution)"

                messages = request.session.pop('messages', None)

                send_mail(subject=f'Contacting From Orange {request.user}',
                          message=form.cleaned_data['body'],
                          from_email=DEFAULT_FROM_EMAIL,
                          recipient_list=['trading3526@gmail.com'],
                          fail_silently=False)

                context = {'messages': messages}
                return render(request, 'intro_script.html', context)

            else:
                print("Why ain't u authenticated??")

        return render(request, 'contacting.html', {'form': form})


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


def save_time_spent(request):
    if request.user.is_authenticated:
        total_time_spent = request.session.get('total_time_spent', 0)

        page_visits = RequestsLog.objects.order_by('-request_time')

        if page_visits.count() > 1:
            page_visit = page_visits[1]
        else:
            page_visit = None

        if page_visit:
            page_visit.duration = timedelta(seconds=total_time_spent)
            page_visit.save()
