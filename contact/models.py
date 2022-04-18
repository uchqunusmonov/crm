from accounts.models import Employe
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(Employe, on_delete=models.CASCADE)
    user_saver = models.ForeignKey(Employe, on_delete=models.CASCADE)
    
    
    