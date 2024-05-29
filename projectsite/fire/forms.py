from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions


class FirestationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"


class FiretruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"


class FirefightersForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'date_time', 'severity_level', 'description']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
            

class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"
        
        
class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'date_time', 'severity_level', 'description']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }


class WeatherConditionsForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"