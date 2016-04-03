from __future__ import unicode_literals

from django.db import models
<<<<<<< HEAD
from django import forms

=======
<<<<<<< HEAD
from django.contrib.auth.models import User
# Create your models here.
=======
>>>>>>> 74faabc6237af03b31aac0e527ac84a74f5b2f07
>>>>>>> 6d39647095ba11331c4edb7ba22bee7fd2c4c4ab

class myuser (models.Model):
	user = models.ForeignKey(User, unique=True)
	dob  	=models.DateField('Date of birth ')
	gender  =models.CharField(max_length=10)
	country =models.CharField(max_length=50)
	city 	=models.CharField(max_length=50)
	region 	=models.CharField(max_length=50)
	accType =models.CharField(max_length=1)
<<<<<<< HEAD
#def __str__(self):
 #   return self.fname

class clinic (models.Model):
	owner	= models.ForeignKey(User, on_delete=models.CASCADE)
	dname 	= models.CharField(max_length=50)  # Dr name
	name    = models.CharField(max_length=50 , default='')
	logo    = models.CharField(max_length=50, default='')
 	dQlfy 	= models.CharField(max_length=100) # Dr Qualification
	cSpec 	= models.CharField(max_length=50) # clinic specialization
	price 	= models.IntegerField(default=0)  # clinic price 
	wtf   	= models.DateTimeField('working time from')
	wtt   	= models.DateTimeField('workign time to')
	country = models.CharField(max_length=50)
	city 	= models.CharField(max_length=50)
	region 	= models.CharField(max_length=50)
	notes	= models.CharField(max_length=500)
	phone	= models.CharField(max_length=50)
	total_ranks=models.IntegerField(default=0)
	users_rated=models.IntegerField(default=0)

# def __str__(self):
#     return self.name

class lab (models.Model):
	owner	= models.ForeignKey(User , on_delete=models.CASCADE)
=======

	def __str__(self):
		return self.fname

class property (models.Model):
	owner	= models.ForeignKey(myuser , on_delete=models.CASCADE)
>>>>>>> 74faabc6237af03b31aac0e527ac84a74f5b2f07
	name    = models.CharField(max_length=50)
	logo    = models.CharField(max_length=50, default='')
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
        	abstract = True


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


<<<<<<< HEAD
class hospital (models.Model):
	owner	= models.ForeignKey(User , on_delete=models.CASCADE)
	name    = models.CharField(max_length=50)
	logo    = models.CharField(max_length=50)
	wtf   	= models.DateTimeField('working time from')
	wtt   	= models.DateTimeField('workign time to')
	country = models.CharField(max_length=50)
	city 	= models.CharField(max_length=50)
	region 	= models.CharField(max_length=50)
	notes	= models.CharField(max_length=500)
	phone	= models.CharField(max_length=50)
	total_ranks=models.IntegerField(default=0)
	users_rated=models.IntegerField(default=0)
 
# def __str__(self):
#     return self.name
=======

>>>>>>> 74faabc6237af03b31aac0e527ac84a74f5b2f07
