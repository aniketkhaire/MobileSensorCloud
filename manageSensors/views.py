from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from user.models import UserSensorData, AvailableSensorData, UserDetails

def  manageSensors(request):
    user_sensor_data = UserSensorData.objects.all()
    available_sensor_data = AvailableSensorData.objects.all()
    return render(request, 'manageSensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})

def addSensor(request, pk):
    available_sensor_data = AvailableSensorData.objects.all()
    sensorData = available_sensor_data.get(id=pk)
    newSensor = UserSensorData()
    newSensor.sensor_name = sensorData.sensor_name
    newSensor.sensor_type = sensorData.sensor_type
    newSensor.sensor_location = sensorData.sensor_location
    newSensor.sensor_provider = sensorData.sensor_provider
    newSensor.sensor_status = sensorData.sensor_status

    user = UserDetails.objects.get(user_name="rishi")
    newSensor.user = user
    newSensor.save()

    user_sensor_data = UserSensorData.objects.all()
    return render(request, 'manageSensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})

def  deleteSensor(request, pk):
    sensor = UserSensorData.objects.filter(id=pk)
    sensor.delete()
    user_sensor_data = UserSensorData.objects.all()
    available_sensor_data = AvailableSensorData.objects.all()
    return render(request, 'manageSensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})

# class AlbumDelete(DeleteView):
#     model = UserSensorData
#     success_url = reverse_lazy('manageSensors:manageSensors$')


