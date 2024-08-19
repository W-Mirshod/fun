from django.views import View
from django.shortcuts import render


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


class OrangePage(View):
    def get(self, request):
        return render(request, 'orange_style.html')


class FireFlyPage(View):
    def get(self, request):
        return render(request, 'firefly_style.html')


class JustHomePage(View):
    def get(self, request):
        return render(request, 'home_script.html')


class TreePage(View):
    def get(self, request):
        return render(request, 'tree_style.html')
