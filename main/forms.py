# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from main.models import CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")


class LogInForm(forms.Form):
    login_name = forms.CharField(max_length=150)
    login_password = forms.CharField(widget=forms.PasswordInput)
