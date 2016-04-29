from django.shortcuts import render
from django.views.generic import View
from MobileSensorCloud.utils import query
from user.models import UserSensorDetail
import json


def createJson(result):
    available_points = list(result.get_points(measurement='sensor_data'))
    entries = []
    for data in available_points:
        timeVal = data['time']
        value = data['value']
        entries.append({"Time":timeVal, "Value": value})
    json_obj = json.dumps(entries)
    return json_obj

class ShowMonitorView(View):
    def get(self, request):
        typeOfSensor = 'sea_water_temperature'
        result = query('select time,value from sensor_data')
        jsonObj= createJson(result)
        user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
        return render(request, 'monitor.html', {'jsonObj':jsonObj, 'user_sensors': user_sensor_data})
