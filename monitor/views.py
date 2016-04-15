from django.shortcuts import render
from django.views.generic import View
import json
from MobileSensorCloud.utils import query

def  monitor(request):
    return render(request, 'monitor.html', {})

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
        # print result
        jsonObj= createJson(result)
        print jsonObj

        return render(request, 'monitor.html', {'jsonObj':jsonObj})
