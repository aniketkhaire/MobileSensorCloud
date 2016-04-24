from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user.models import UserSensorDetail
import json

@login_required()
def dashboard(request):
    sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
    latlongdata = []
    for sensor in sensor_data:
        singledata = []
        singledata.append(str(sensor.sensor_id.location))
        singledata.append(sensor.sensor_id.latitude)
        singledata.append(sensor.sensor_id.longitude)
        latlongdata.append(singledata)
    print latlongdata
    return render(request, 'dashboard.html', {'sensor_data': sensor_data, 'latlongdata': json.dumps(latlongdata)})
