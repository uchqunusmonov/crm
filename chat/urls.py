from django.urls import path

from .views import *


urlpatterns = [
    path('', chat, name='chat'),
    path('send-message/', send_message, name='send-message'),
]
