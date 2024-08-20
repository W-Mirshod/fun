from django.views import View
from django.shortcuts import render, redirect


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')


class ChoicesPage(View):
    def get(self, request):
        return render(request, 'button_index.html')


class BloomingFlowersPage(View):
    def get(self, request):
        return render(request, 'blooming.html')


class CalmingHomePage(View):
    def get(self, request):
        return render(request, 'calming_style.html')


class SolarSystemPage(View):
    def get(self, request):
        return render(request, 'universe_index.html')


# class OrangePage(View):
#     def get(self, request):
#         return render(request, 'orange_style.html')

def intro_page(request):
    if request.method == 'GET':
        return render(request, 'intro_style.html')


def alerting(request):
    if request.method == 'GET':
        request.session['popup_message'] = \
            "You currently can not enter this page. Sorry but it is not fully done yet, Orange)"
        popup_message = request.session.pop('popup_message', None)
        if not popup_message:
            redirect('choices')
        context = {'popup_message': popup_message}

        return render(request, 'alert.html', context)


class FireFlyPage(View):
    def get(self, request):
        return render(request, 'firefly_style.html')


class JustHomePage(View):
    def get(self, request):
        return render(request, 'home_script.html')


class TreePage(View):
    def get(self, request):
        return render(request, 'tree_style.html')


def my_view(request):
    if request.method == 'GET':
        # Option 1: Using session
        request.session['popup_message'] = "This is a popup message."
        return redirect('choices')
    return render(request, 'intro_style.html')
