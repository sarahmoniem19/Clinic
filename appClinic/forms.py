from django import forms
from .models import lab
from django.contrib.auth.models import User
from django.forms import ModelForm

class nameForm(forms.Form):
	yourName=forms.CharField(label="Your name",max_length=20)


class LabForm(ModelForm):
	class Meta:
		model = lab
		exclude = ('lab',)
		fields = ['owner','name','logo','wtf','wtt','country','city','region',
				'notes','phone']

class registerForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password']
	dob = forms.DateField(label="Date of Birth" )
	gender = forms.CharField(label="Gender",max_length=20)
	country =forms.CharField(label="Country",max_length=50)
	city 	=forms.CharField(label="City",max_length=50)
	region 	=forms.CharField(label="Region",max_length=50)
	accType =forms.CharField(label="Account type",max_length=1)


