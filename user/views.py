import datetime

from django.views.generic import View
from user.forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from MobileSensorCloud.utils import write_points

class UserLoginView(View):
    form_class = LoginForm
    template_name = 'login.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Submit form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.save()
            # To change password - user.set_password(password)

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard:dashboard')
                    #This is logs in with session handling
                    #User request.user to get info

        return render(request, self.template_name, {'form': form})


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'user_register.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Submit form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # cleaned (normalized) data
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            json_body = [{
                'measurement': 'user_data',
                'tags': {'username': username, },
                'fields': {'name': name, 'password': password, 'email': email },
                }]
            write_points(json_body)
            return redirect('dashboard:dashboard')

        return render(request, self.template_name, {'form': form})
