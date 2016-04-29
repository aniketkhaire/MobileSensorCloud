from django import forms
from sensor_owner.models import SensorDetail, SensorType, SensorUnit


class AddSensorForm(forms.ModelForm):
    station_name = forms.CharField(max_length=400)
    station_desc=forms.CharField(max_length=800)
    active = forms.BooleanField(initial=True)
    location = forms.CharField(max_length=400)
    latitude = forms.CharField(max_length=10)
    longitude = forms.CharField(max_length=10)
    url = forms.CharField(max_length=800)

    class Meta:
        model = SensorDetail
        fields = ['station_name', 'station_desc', 'sensor_type', 'sensor_unit', 'active', 'location', 'latitude', 'longitude', 'url']