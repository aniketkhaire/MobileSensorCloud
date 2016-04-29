from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import UserDetail


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    roles = [('sys_admin', 'Admin'), ('sensor_owner', 'Sensor Owner'), ('end_user', 'User')]

    user_role = forms.ChoiceField(widget=forms.RadioSelect, choices=roles)

    class Meta:
        model = User
        fields = ['username', 'password', 'user_role']

    def clean(self):
        username = self.cleaned_data.get('username', None)
        password = self.cleaned_data.get('password', None)
        role = self.cleaned_data.get('user_role', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Username or Password is incorrect")
        if not UserDetail.objects.filter(user_name=username, user_role=role).exists():
            raise forms.ValidationError("Invalid user role")
        return self.cleaned_data

class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    roles = [('sys_admin', 'Admin'), ('sensor_owner', 'Sensor Owner'), ('end_user', 'User')]

    user_role = forms.ChoiceField(widget=forms.RadioSelect, choices=roles)

    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email', 'user_role']