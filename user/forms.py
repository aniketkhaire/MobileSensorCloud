from django.contrib.auth.models import User
from django import forms
from .models import UserDetails, LoginCredentials

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    roles = [('sys_admin', 'Admin'), ('sensor_owner', 'Sensor Owner'), ('user', 'User')]

    user_role = forms.ChoiceField(widget=forms.RadioSelect, choices=roles)

    class Meta:
        model = LoginCredentials
        fields = ['username', 'password', 'user_role']

class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    roles = [('sys_admin', 'Admin'), ('sensor_owner', 'Sensor Owner'), ('user', 'User')]

    user_role = forms.ChoiceField(widget=forms.RadioSelect, choices=roles)

    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'password', 'email', 'user_role']