from django import forms
from .models import lab
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
		fields = ['owner','name','logo','wtf','wtt','country','city','region','notes','phone']
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
		
		
		