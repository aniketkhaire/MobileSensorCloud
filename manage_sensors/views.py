from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from user.models import UserDetail, UserSensorDetail
from sensor_owner.models import SensorDetail


def  manage_sensors(request):
    user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user).values('sensor_id').get(se)
    available_sensor_data = SensorDetail.objects.all()
    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})


def add_sensor(request, pk):
    available_sensor_data = SensorDetail.objects.all()
    sensor_data = available_sensor_data.get(id=pk)
    current_user = request.user

    new_sensor = UserSensorDetail()
    new_sensor.user_name = current_user
    new_sensor.sensor_id = sensor_data
    new_sensor.save()

    user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})


def  delete_sensor(request, pk):
    sensor = UserSensorDetail.objects.get(id=pk)
    sensor.delete()
    user_sensor_data = (UserSensorDetail.objects.filter(user_name=request.user)).values('sensor_id')

    available_sensor_data = SensorDetail.objects.all()
    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})

