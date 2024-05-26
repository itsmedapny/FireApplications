from django.contrib import admin
from django.urls import path
from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, map_incidents, FireStationList, FireStationAdd, FireStationUpdate, FireStationDelete


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
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
]