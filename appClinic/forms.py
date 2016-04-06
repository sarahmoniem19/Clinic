from django import forms
from .models import *
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
		
class hospitalForm(ModelForm):
	class Meta:
		model = hospital
		fields = ['name','logo','wtf','wtt','country','city','region','notes','phone']

		
class registerForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password']

class registerf(ModelForm):
	class Meta:
		model = myuser
		fields = ['dob','gender','country','city','region','accType']



