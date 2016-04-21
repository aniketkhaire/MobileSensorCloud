from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from user.models import UserDetail
from sensor_owner.models import SensorDetails

def  manageSensors(request):
    #user_sensor_data = UserSensor.objects.all()
    available_sensor_data = SensorDetails.objects.all()
    return render(request, 'manageSensors.html', {'available_sensors': available_sensor_data})

def addSensor(request, pk):
    # available_sensor_data = AvailableSensorData.objects.all()
    # sensorData = available_sensor_data.get(id=pk)
    # newSensor = UserSensor()
    # newSensor.sensor_name = sensorData.sensor_name
    # newSensor.sensor_type = sensorData.sensor_type
    # newSensor.sensor_location = sensorData.sensor_location
    # newSensor.sensor_provider = sensorData.sensor_provider
    # newSensor.sensor_status = sensorData.sensor_status
    #
    # user = UserDetail.objects.get(user_name="rishi")
    # newSensor.user = user
    # newSensor.save()
    #
    # user_sensor_data = UserSensor.objects.all()
    return render(request, 'manageSensors.html', {})#{'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})

def  deleteSensor(request, pk):
    # sensor = UserSensor.objects.filter(id=pk)
    # sensor.delete()
    # user_sensor_data = UserSensor.objects.all()
    # available_sensor_data = AvailableSensorData.objects.all()
    return render(request, 'manageSensors.html', {})

# class AlbumDelete(DeleteView):
#     model = UserSensorData
#     success_url = reverse_lazy('manageSensors:manageSensors$')


