from django.urls import path, re_path

from tasks.views import *

urlpatterns = [
    path('calendar/<str:username>/', calendar, name='calendar' ),
    path('add_task/<str:username>', add_task, name='add_task'),
    path('update', update, name='update'),
    path('get-tasks/', get_tasks, name='get-tasks'),
    path('update-task/<str:username>/<int:pk>/', update_task, name='update_task'),
    path('all_tasks/<str:username>', all_tasks, name='all_tasks'),
    path('task/<str:username>/', task, name='task'),
    path('delete-task/<slug:slug>/', delete, name='delete-task'),
]