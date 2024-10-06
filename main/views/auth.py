from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib import messages
from main.forms import SignUpForm, LogInForm
from main.models import CustomUser
from main.views.pages import send_sms


class SignUpView(CreateView):
    model = CustomUser
    template_name = "auth.html"
    form_class = SignUpForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        send_sms(self.request, 'Signed In')
        login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please check the information.')
        return super().form_invalid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        send_sms(request, 'Log In')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'auth.html')
