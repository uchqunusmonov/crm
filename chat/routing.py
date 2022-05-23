from . import consumers
from django.urls import re_path as url

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),   # esda tursin
    url(r'^ws/personal_chat/(?P<room_name>[^/]+)/$', consumers.PersonalConsumer.as_asgi()),
]