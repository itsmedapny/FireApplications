from django.contrib import admin
from django.urls import path
from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, map_incidents, FireStationList, FireStationAdd, FireStationUpdate, FireStationDelete, FireTruckList, FireTruckAdd, FireTruckUpdate, FireTruckDelete, FireFightersList, FireFightersAdd, FireFightersUpdate, FireFightersDelete, IncidentsList, IncidentsAdd, IncidentsUpdate, IncidentsDelete, LocationsList, LocationsAdd, LocationsUpdate, LocationsDelete, WeathersList, WeathersAdd, WeathersUpdate, WeathersDelete

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='dashboard-chart'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('stations', map_station, name='map-station'),
    path('incidents', map_incidents, name='map-incidents'),
    path('weather_list', FireStationList.as_view(), name='firestation-list'),
    path('weather_list/add', FireStationAdd.as_view(), name='firestation-add'),
    path('weather_list/edit/<int:pk>', FireStationUpdate.as_view(), name='firestation-update'),
    path('weather_list/delete/<int:pk>', FireStationDelete.as_view(), name='firestation-delete'),
    path('fire_truck', FireTruckList.as_view(), name='firetruck-list'),
    path('fire_truck/add', FireTruckAdd.as_view(), name='firetruck-add'),
    path('fire_truck/edit/<int:pk>', FireTruckUpdate.as_view(), name='firetruck-update'),
    path('fire_truck/delete/<int:pk>', FireTruckDelete.as_view(), name='firetruck-delete'),
    path('firefighters', FireFightersList.as_view(), name='firefighters-list'),
    path('firefighters/add', FireFightersAdd.as_view(), name='firefighters-add'),
    path('firefighters/edit/<int:pk>', FireFightersUpdate.as_view(), name='firesfighters-update'),
    path('firefighters/delete/<int:pk>', FireFightersDelete.as_view(), name='firesfighters-delete'),
    path('incidentslist', IncidentsList.as_view(), name='incidents-list'),
    path('incidentslist/add', IncidentsAdd.as_view(), name='incidents-add'),
    path('incidentslist/edit/<int:pk>', IncidentsUpdate.as_view(), name='incidents-update'),
    path('incidentslist/delete/<int:pk>', IncidentsDelete.as_view(), name='incidents-delete'),
    path('locationslist', LocationsList.as_view(), name='locations-list'),
    path('locationslist/add', LocationsAdd.as_view(), name='locations-add'),
    path('locationslist/edit/<int:pk>', LocationsUpdate.as_view(), name='locations-update'),
    path('locationslist/delete/<int:pk>', LocationsDelete.as_view(), name='locations-update'),
    path('weatherslist', WeathersList.as_view(), name='weathers-list'),
    path('weatherslist/add', WeathersAdd.as_view(), name='weathers-add'),
    path('weatherslist/edit/<int:pk>', WeathersUpdate.as_view(), name='weathers-update'),
    path('weatherslist/delete/<int:pk>', WeathersDelete.as_view(), name='weathers-delete'),
]