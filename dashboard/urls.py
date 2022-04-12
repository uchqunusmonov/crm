from django.urls import path
<<<<<<< HEAD

from .views import dashboard





urlpatterns = [
    path('dashboard/<str:username>/',dashboard, name='dashboard')
]
=======
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
]
>>>>>>> 7f2061c7ab5ff73ea00efc0c281c5298dd14c277
