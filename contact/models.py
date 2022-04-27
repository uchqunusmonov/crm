from accounts.models import Employe
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    add_contact = models.ForeignKey(Employe, on_delete=models.CASCADE)
    add_contact_to = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name="my_contacts")