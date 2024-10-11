from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from main.models import CustomUser
# from django.views.generic import CreateView
#
# from main.forms import SignUpForm
from main.views.pages import send_sms


# class SignUpView(CreateView):
#     model = User
#     template_name = "auth.html"
#     form_class = SignUpForm
#     success_url = "/"
#
#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.is_staff = False
#         user.is_superuser = False
#         user.save()
#         send_sms(self.request, 'Signed In')
#         login(self.request, user)
#
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.error(self.request, 'Registration failed. Please check the information.')
#         return super().form_invalid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password').lower()

        send_sms(request, 'Log In')

        if password == 'bitliqi' or request.user.is_superuser:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                CustomUser.objects.create_user(username=username, password=password)
                user = authenticate(request, username=username, password=password)
                login(request, user)

                messages.success(request, "Successfully Created A New Account")

                return redirect('index')

        elif password == 'password':
            messages.error(request, 'I said this is too easy to guess (')

        else:
            messages.error(request, 'Invalid password.')

    return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return redirect('login')
