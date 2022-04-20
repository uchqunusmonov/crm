from django.db import models
from django.utils.text import slugify
# Create your models here.
from accounts.models import *
class Task(models.Model):

    choice = (
        ('',''),
        ('in progress','in progress'),
        ('completed','completed'),
        ('not completed','not completed'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    employe = models.ManyToManyField(Employe, blank=True)
    creator = models.ForeignKey(Employe, on_delete=models.PROTECT, related_name='creators', blank=True)
    checker = models.ManyToManyField(Employe, related_name='checkers', blank=True)
    active = models.BooleanField(default=False)
    upload = models.DateTimeField(blank=True, null=True)
    section = models.ManyToManyField(Section, blank=True)
    status = models.CharField(max_length=100, choices=choice, default=False, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)


    def save(self, *args, **kwargs):
        
        slug = f'{self.name}'


        self.slug = slugify(slug)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.creator)
