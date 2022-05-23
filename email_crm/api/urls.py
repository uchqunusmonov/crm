from django.urls import path
from . import views


urlpatterns = [
    path('email-send/', views.EmailList.as_view(), name='email-send'),
    path('get-archived-emails/<int:pk>/', views.GetArchivedEmails.as_view(), name='get-archived-emails'),
    path('get-sent-emails/<int:pk>/', views.GetSentEmails.as_view(), name='get-sent-emails'),
]
