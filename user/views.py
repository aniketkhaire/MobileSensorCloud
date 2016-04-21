from django.views.generic import View
from user.forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from models import UserDetail, UserRole


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
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_role = form.cleaned_data['user_role']

            role = UserRole.objects.get(role=user_role)
            user = authenticate(username=username, password=password)

            if user is not None and role is not None:
                if user.is_active:
                    login(request, user)
                    if role.role == "sensor_owner":
                        return redirect('sensor_owner:ownerDashboard')
                    elif role.role == "sys_admin":
                        return redirect('sensor_admin:sensor_admin')
                    else:
                        print "Redirecting User"
                        url = reverse("dashboard:dashboard")
                        return redirect(url)

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
            user_role = form.cleaned_data['user_role']

            # Login credentials in the default User table
            user.first_name = name
            user.set_password(password)
            user.save()

            # Other user details
            userDetail = UserDetail()
            userDetail.user_name = username
            userDetail.user_role = user_role
            userDetail.email = email
            userDetail.name = name
            userDetail.save()

            return redirect('user:login')

        return render(request, self.template_name, {'form': form})


def logoutView(request):
    print "Logging out"
    logout(request)
    print request.user.is_authenticated()
    return redirect('user:login')
