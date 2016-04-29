from django.shortcuts import render
from sensor_owner.models import SensorDetail
from user.models import UserSensorDetail
import json

# Create your views here.

def sensorAdmin(request):
    sensor_data = SensorDetail.objects.all()
    latlongdata = []
    for sensor in sensor_data:
        singledata = []
        singledata.append(str(sensor.location))
        singledata.append(sensor.latitude)
        singledata.append(sensor.longitude)
        latlongdata.append(singledata)

    sensortypes = []
    header = []
    header.append("Sensor")
    header.append("Count")
    sensortypes.append(header)

    header = []
    header.append('Temperature')
    header.append(11)
    sensortypes.append(header)

    header = []
    header.append('Turbidity')
    header.append(8)
    sensortypes.append(header)

    header = []
    header.append('Salinity')
    header.append(2)
    sensortypes.append(header)

    header = []
    header.append('Pressure')
    header.append(4)
    sensortypes.append(header)

    return render(request, 'admin_dashboard.html', {'sensor_data': sensor_data, 'latlongdata': json.dumps(latlongdata),
                                                    'sensor_types': json.dumps(sensortypes)})

def manageAvailableSensors(request):
    user_sensor_data = UserSensorDetail.objects.all()
    sensor_data = SensorDetail.objects.all()
    return render(request, 'admin_manage_sensors.html', {'available_sensors': sensor_data, 'user_sensors': user_sensor_data})

def manageAvailableUsers(request):
    #TODO Add table for user billing or just take data from two tables and show
    return render(request, 'manage_users.html', {})
