from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets        
from django.contrib.admin.widgets import AdminDateWidget
from datetimewidget.widgets import TimeWidget

class nameForm(forms.Form):
	yourName=forms.CharField(label="Your name",max_length=20)
	class Meta:
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
#-------------------------- Add Lab  Form ------------------#		
class LabForm(ModelForm):
	class Meta:
		model = lab

		fields = ['name','logo','wtf','wtt','country','city','region','notes','phone']
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		widgets = {
			#Use localization and bootstrap 3
			'wtt': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
			'wtf': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
		}	
	#
	def clean(self):
		pass

#-------------------------- Registration  Form ------------------#		
	def __init__(self, *args, **kwargs):
		super(LabForm, self).__init__(*args, **kwargs)
		# self.fields['wtf'].widget = widgets.AdminSplitDate()
		# self.fields['wtt'].widget = widgets.AdminSplitDate()
		
		
		
class registerForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password']
		widgets = {
            'password': forms.PasswordInput(),
        }


class registerf(ModelForm):
	class Meta:
		model = myuser
		fields = ['dob','gender','country','city','region','accType']
		widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
        }
#-------------------------- Add Hospital  Form ------------------#				
class HosForm(ModelForm):
	class Meta:
		model = hospital

		fields = ['name','logo','wtf','wtt','country','city','region','notes','phone']
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		widgets = {
			#Use localization and bootstrap 3
			'wtt': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
			'wtf': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
		}


class CliForm(ModelForm):
	class Meta:
		model = clinic
		fields = ['name','logo','wtf','wtt','country','city','region','notes','phone','dname','dQlfy','cSpec','price']
		error_messages={
		NON_FIELD_ERRORS:{
			'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		
		widgets = {
			#Use localization and bootstrap 3
			'wtt': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
			'wtf': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
		}

