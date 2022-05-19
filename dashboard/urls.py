from django.urls import path

from .views import dashboard, get_weather_json, get_data





urlpatterns = [
    path('dashboard/<str:username>/',dashboard, name='dashboard'),
    path('weather', get_weather_json, name="get_weather_json"),
    path('dashboard/<str:username>/get_data/', get_data , name='get_data')
]
