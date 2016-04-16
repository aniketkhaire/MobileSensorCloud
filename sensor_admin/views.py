from django.shortcuts import render
from user.models import UserSensorData

# Create your views here.

def sensorAdmin(request):
    sensor_data = UserSensorData.objects.all().filter()
    return render(request, 'admin.html', {'sensor_data':sensor_data})
