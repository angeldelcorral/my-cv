from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Skills(models.Model):
	
	kind = models.ChartField(max_length=50)
	description = models.ChartField(max_length=100)
	level = models.PositiveImtegerField()
	