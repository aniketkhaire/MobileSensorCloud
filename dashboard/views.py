from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    sensor_data = ''
    return render(request, 'dashboard.html', {'sensor_data': sensor_data})
