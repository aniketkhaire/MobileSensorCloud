from django.shortcuts import render

# Create your views here.

def sensorAdmin(request):
    #sensor_data = UserSensor.objects.all().filter()
    return render(request, 'admin.html', {})

def manageAvailableSensors(request):
    #sensor_data = UserSensor.objects.all().filter()
    return render(request, 'manage_sensors.html', {})

def manageAvailableUsers(request):
    return render(request, 'manage_users.html', {})
