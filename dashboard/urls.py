from django.urls import path

from .views import dashboard, get_weather_json





urlpatterns = [
    path('dashboard/<str:username>/',dashboard, name='dashboard'),
    path('weather', get_weather_json, name="get_weather_json"),
]
