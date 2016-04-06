from __future__ import unicode_literals

from django.db import models
from django import forms

from django.contrib.auth.models import User

class myuser (models.Model):
	user = models.OneToOneField(User, unique=True)
	dob  	=models.DateField('Date of birth ')
	gender  =models.CharField(max_length=10)
	country =models.CharField(max_length=50)
	city 	=models.CharField(max_length=50)
	region 	=models.CharField(max_length=50)
	accType =models.CharField(max_length=1)




class property (models.Model):
	owner	= models.ForeignKey(myuser , on_delete=models.CASCADE)
	name    = models.CharField(max_length=50)
	logo    = models.ImageField(null=True,blank=True)
	wtf   	= models.DateTimeField('working time from')
	wtt   	= models.DateTimeField('workign time to')
	country = models.CharField(max_length=50)
	city 	= models.CharField(max_length=50)
	region 	= models.CharField(max_length=50)
	notes	= models.CharField(max_length=500)
	phone	= models.CharField(max_length=50)
	total_ranks=models.IntegerField(default=0)
	users_rated=models.IntegerField(default=0)

	class Meta:
		abstract=True


class clinic (property):
	dname 	= models.CharField(max_length=50)  # Dr name
	dQlfy 	= models.CharField(max_length=100) # Dr Qualification
	cSpec 	= models.CharField(max_length=50)  # clinic specialization
	price 	= models.IntegerField(default=0)   # clinic price

class lab (property):
	pass
class hospital (property):
	pass
class labAnalysis (models.Model):
	labId	= models.ForeignKey(lab , on_delete=models.CASCADE)
	type 	= models.CharField(max_length=100)
	price	= models.IntegerField(default=0)


