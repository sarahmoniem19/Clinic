from __future__ import unicode_literals

from django.db import models


# Create your models here.


class myuser (models.Model):
	fname	=models.CharField(max_length=50)
	lname	=models.CharField(max_length=50)
	dob  	=models.DateTimeField('Date of birth ')
	gender  =models.CharField(max_length=10)
	password=models.CharField(max_length=50)
	email	=models.CharField(max_length=50)
	country =models.CharField(max_length=50)
	city 	=models.CharField(max_length=50)
	region 	=models.CharField(max_length=50)
	accType =models.CharField(max_length=1)

#def __str__(self):
 #   return self.fname

class clinic (models.Model):
	owner	= models.ForeignKey(myuser, on_delete=models.CASCADE)
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
	owner	= models.ForeignKey(myuser , on_delete=models.CASCADE)
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

class labAnalysis (models.Model):
	labId	= models.ForeignKey(lab , on_delete=models.CASCADE)
	type 	= models.CharField(max_length=100)
	price	= models.IntegerField(default=0)

# def __str__(self):
#     return self.type

class hospital (models.Model):
	owner	= models.ForeignKey(myuser , on_delete=models.CASCADE)
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
