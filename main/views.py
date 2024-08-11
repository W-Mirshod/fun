from django.views import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ChoicesPage(View):
    def get(self, request):
        return render(request, 'choices.html')


class BloomingFlowersPage(View):
    def get(self, request):
        return render(request, 'blooming.html')
