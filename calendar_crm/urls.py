from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('calendar/<str:username>/', calendar, name='calendar' ),
    re_path('^add_event$', add_event, name='add_event'),
    re_path('^update$', update, name='update'),
    path('remove', remove, name='remove'),
    re_path('^all_events', all_events, name='all_events')

]
