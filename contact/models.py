from accounts.models import Employe
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(Employe, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='contact/images', null=True, blank=True)
    
    