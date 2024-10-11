# forms.py
from django import forms

from main.models import CustomUser, Contacting


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

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if CustomUser.objects.filter(password=password).exists():
            raise forms.ValidationError("This password is already in use. Please choose a different one.")
        return password


class LogInForm(forms.Form):
    login_name = forms.CharField(max_length=150)
    login_password = forms.CharField(widget=forms.PasswordInput)


class ContactingForm(forms.ModelForm):
    class Meta:
        model = Contacting
        fields = ['body']
