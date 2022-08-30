from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, IntegerField, FloatField
from django.db import models
from django.urls import reverse


class KPI(models.Model):
		description = models.CharField(max_length=200)
		amount = models.FloatField()
		date = models.DateTimeField(auto_now_add=True)
		author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)
	
		def __str__(self):
			return f'{self.description} - {self.amount}'
		
		def get_absolute_url(self):
			return reverse('kpi_detail', args=[str(self.id)])

class Performance(models.Model):
		description = models.CharField(max_length=200)
		amount = models.IntegerField()
	
		def __str__(self):
			return f'{self.description} - {self.amount}'

class Deposit(models.Model):
		description = models.CharField(max_length=200)
		amount = models.IntegerField()
		date = models.DateTimeField(auto_now_add=True)
		author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
		)
	
		def __str__(self):
			return f'{self.description} - {self.amount}'
		
		def get_absolute_url(self):
			return reverse('deposit_detail', args=[str(self.id)])

class Loan(models.Model):
		description = models.CharField(max_length=200)
		amount = models.IntegerField()
	
		def __str__(self):
			return f'{self.description} - {self.amount}'

class Income(models.Model):
		description = models.CharField(max_length=200)
		amount = models.IntegerField()
	
		def __str__(self):
			return f'{self.description} - {self.amount}'

class Expense(models.Model):
		description = models.CharField(max_length=200)
		amount = models.IntegerField()
	
		def __str__(self):
			return f'{self.description} - {self.amount}'