from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, default='')
    first_name = models.CharField(max_length=60, default='')
    last_name = models.CharField(max_length=60, default='')
    address = models.CharField(max_length=120, default='')
    city = models.CharField(max_length=60, default='')
    country = models.CharField(max_length=40,default='')
    cell_phone = models.CharField(max_length=18, default='')
    phone = models.CharField(max_length=18, default='')
    birthdate = models.DateField(blank=True, null=True)

    pic_height = models.PositiveIntegerField(default=150)
    pic_width = models.PositiveIntegerField(default=150)
    pic_profile = models.ImageField(upload_to='media/images/profile_img', default='', width_field='pic_width', height_field='pic_height')


