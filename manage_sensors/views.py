from django.shortcuts import render
from user.models import UserSensorDetail
from sensor_owner.models import SensorDetail


def is_sensor_present(request, sensor_data):
    if UserSensorDetail.objects.filter(user_name=request.user, sensor_id=sensor_data).exists():
        return True
    else:
        return False


def manage_sensors(request):
    user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
    available_sensor_data = SensorDetail.objects.all()
    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data})


def add_sensor(request, pk):
    available_sensor_data = SensorDetail.objects.all()
    sensor_data = available_sensor_data.get(id=pk)
    current_user = request.user
    error_message = ''
    success_message = ''
    if is_sensor_present(request, sensor_data):
        error_message = 'Sensor already subscribed'
    else:
        new_sensor = UserSensorDetail()
        new_sensor.user_name = current_user
        new_sensor.sensor_id = sensor_data
        new_sensor.save()
        success_message = 'Sensor with ID '+ str(sensor_data.sensor_id) + ' subscribed'

    user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data,
                                                   'error_message': 'Sensor already subscribed', 'error_message': error_message,
                                                   'success_message': success_message})


def delete_sensor(request, pk):
    sensor = UserSensorDetail.objects.get(id=pk)
    sensor.delete()

    user_sensor_data = UserSensorDetail.objects.filter(user_name=request.user)
    available_sensor_data = SensorDetail.objects.all()
    success_message = 'Sensor deleted'

    return render(request, 'manage_sensors.html', {'user_sensors': user_sensor_data, 'available_sensors': available_sensor_data,
                                                   'success_message': success_message})

