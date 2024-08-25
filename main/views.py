from django.shortcuts import render, redirect


def home_page(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def choices_page(request):
    if request.method == 'GET':
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
