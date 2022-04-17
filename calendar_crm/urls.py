from .views import *
from django.urls import path


urlpatterns = [
    path('calendar/<str:username>/', calendar, name='calendar' ),
]
