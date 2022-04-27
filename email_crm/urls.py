import email
from django.urls import path

from email_crm.views import email_send

urlpatterns = [
     path('', email_send, name= 'email-box'),
]
