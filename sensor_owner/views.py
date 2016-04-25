from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from sensor_owner.forms import AddSensorForm
from sensor_owner.models import SensorDetail
import random


class ShowSensorsView(View):
    template_name='sensor_owner_home.html'

    def get(self,request):
        user = request.user
        available_sensors = SensorDetail.objects.filter(sensorOwner=user)
        return render(request, 'sensor_owner_home.html', {'available_sensors':available_sensors})


class AddSensorView(View):
    form_class = AddSensorForm
    template_name = 'sensor_owner_manage.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        user = request.user
        available_sensors = SensorDetail.objects.filter(sensorOwner=user)
        return render(request, self.template_name, {'form': form,'available_sensors':available_sensors})

    # Submit form
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            sensor = SensorDetail()

            # cleaned (normalized) data
            sensor.sensor_id = self.get_sensor_Id()
            sensor.station_name = form.cleaned_data['station_name']
            sensor.station_desc = form.cleaned_data['station_desc']
            sensor.sensor_type = form.cleaned_data['sensor_type']
            sensor.sensor_unit = form.cleaned_data['sensor_unit']
            sensor.active = bool(form.cleaned_data['active'])
            sensor.latitude = form.cleaned_data['latitude']
            sensor.longitude = form.cleaned_data['longitude']
            sensor.location = form.cleaned_data['location']
            sensor.url = form.cleaned_data['url']
            sensor.sensorOwner = request.user
            sensor.ip_address = form.cleaned_data['ip_address']
            sensor.save()
            form = self.form_class(None)
        available_sensors = SensorDetail.objects.filter(sensorOwner=request.user)
        return render(request, self.template_name, {'form': form, 'available_sensors':available_sensors,
                                                    'success_message': 'Sensor added successfully'})

    def get_sensor_Id(self):
        sensor_present = True
        while sensor_present:
            try:
                sensor_id = random.randint(99999, 999999)
                SensorDetail.objects.get(sensor_id=sensor_id)
            except SensorDetail.DoesNotExist:
                sensor_present = False
        print "New sensor Id "+ str(sensor_id)
        return sensor_id

