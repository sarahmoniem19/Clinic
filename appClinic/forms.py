from django import forms
from .models import lab
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.admin.widgets import AdminDateWidget

class nameForm(forms.Form):
	yourName=forms.CharField(label="Your name",max_length=20)
	class Meta:
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}

class LabForm(ModelForm):
	class Meta:
		model = lab

<<<<<<< HEAD
		fields = ['name','logo','wtf','wtt','country','city','region','notes','phone']
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		widgets={
			'wtf':AdminDateWidget(),
		}

	#
	def clean(self):
		pass
		
		
		
=======
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


>>>>>>> 6d39647095ba11331c4edb7ba22bee7fd2c4c4ab
