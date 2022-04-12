from django.urls import path

from .views import dashboard





urlpatterns = [
    path('dashboard/<str:username>/',dashboard, name='dashboard')
]