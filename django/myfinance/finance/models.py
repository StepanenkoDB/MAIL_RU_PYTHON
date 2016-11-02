from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Charge(models.Model):
	title = models.CharField(max_length=256)
	amount = models.BigIntegerField()
	date = models.DateTimeField()#default=timezone.now)
	sign = models.BooleanField() # True is income

	def __str__(self):
		return self.title

	def publish(self):
		self.date = timezone.now()
		self.save()
