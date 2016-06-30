from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Eperience(models.Model):

	position = models.ChartField(max_length= 50)
	company = models.ChartField(max_length= 120)
	start = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	description = models.TextField()	