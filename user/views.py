from django.views.generic import View
from user.forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from models import UserSensorData

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
        # cleaned (normalized) data
        username = request.POST['username']
        password = request.POST['password']
        print "Username entered"
        # To change password - user.set_password(password)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                print "User authenticated trying to login"
                login(request, user)

                sensor_data = UserSensorData.objects.all().filter()

                print "after sensor data"

                return render(request, 'dashboard.html', {'sensor_data': sensor_data})
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
            user = form.save(commit=False)

            # cleaned (normalized) data
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.first_name = name
            user.set_password(password)
            user.save()
            return redirect('user:login')
            # To change password - user.set_password(password)

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    return redirect('user:login')
                    #This is logs in with session handling
                    #User request.user to get info

        return render(request, self.template_name, {'form': form})