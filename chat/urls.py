from django.urls import path

from .views import *

from django.views.generic.base import RedirectView


urlpatterns = [
    path('', home, name = 'chat'),
    path('chat/<str:room_name>/', start_chat, name='start_chat'),
]
