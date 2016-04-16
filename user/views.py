from django.views.generic import View
from user.forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from models import UserSensorData, UserDetails, LoginCredentials, UserRoles

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
        user_role = request.POST['user_role']
        print "Username entered"
        # To change password - user.set_password(password)

        try:
            user = LoginCredentials.objects.get(user_detail__user_name=username)
            user_role = user.user_role
        except LoginCredentials.DoesNotExist:
            user = None

        print "Username role "+ user_role.role
        if user is not None:
            if user_role.role == "sensor_owner":
                return redirect('sensor_owner:ownerDashboard')
            elif user_role.role == "sys_admin":
                return redirect('sensor_admin:sensor_admin')
            else:
                sensor_data = UserSensorData.objects.all().filter()
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
            user = UserDetails()

            # cleaned (normalized) data
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user_role = form.cleaned_data['user_role']

            user.user_name = username
            user.name = name
            user.user_role = user_role
            user.email = email
            user.save()

            loginCred = LoginCredentials()
            loginCred.user_detail = user
            loginCred.user_role = UserRoles.objects.get(role=user_role)
            loginCred.password = password
            loginCred.save()

            return redirect('user:login')

        # if form.is_valid():
        #     user = form.save(commit=False)
        #
        #     # cleaned (normalized) data
        #     name = form.cleaned_data['name']
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     email = form.cleaned_data['email']
        #
        #     user.first_name = name
        #     user.set_password(password)
        #     user.save()
        #     return redirect('user:login')
        #     # To change password - user.set_password(password)
        #
        #     user = authenticate(username=username, password=password)
        #
        #     if user is not None:
        #         if user.is_active:
        #             return redirect('user:login')
        #             #This is logs in with session handling
        #             #User request.user to get info

        return render(request, self.template_name, {'form': form})