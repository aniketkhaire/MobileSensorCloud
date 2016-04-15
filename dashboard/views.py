from django.shortcuts import render
from django.contrib.auth import logout

def  dashboard(request):
    return render(request, 'dashboard.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'login.html')
