from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.forms import ModelForm
from appClinic.models import myuser 
from appClinic.models import lab
from .forms import LabForm

# Create your views here.
def getName(request):
	#check if the request post so we need to process the form data
	if request.method=='POST':
		#create the form instance and populate it with data from the request
		form=nameForm(request.POST)
		form.save()
		#check if it's valid
		if form.is_valid():
			#process the data in form.cleand_data
			#redirect to a new URL

			return HttpResponseRedirect('/done/')

	#if any other method we will create blank form
	else:
		form=nameForm()
	

	return render(request,'appClinic/name.html',{'form':form})

def index(request):
	return HttpResponse("Welcome to index")

def yourName(request):

	return HttpResponse("your name is "+request.POST.get("yourName", ""))


def addlap(request):
	if(request.method=='POST'):
		labForm = LabForm(request.POST)	
	else:
		labForm = LabForm()

	return render(request,'appClinic/addLap.html',{'form':labForm})


def lapName(request):
 #I'm the a8baaaa wa7d f el doniaaaaa 

 #Stupid ...........................Stupid

	#done added lap
	if(request.method=='POST'):

			labForm = LabForm(request.POST)
			if labForm.is_valid():
				wtt=request.POST.get('wtt','')
				wtt=wtt.replace('+',' ')

				wtf=request.POST.get('wtf','')
				wtf=wtf.replace('+',' ')

				lab=labForm.save(commit=False)
				user=myuser.objects.get(pk=2)
				
				lab.wtf=wtf
				lab.wtt=wtt
				lab.owner=user
				
				lab.save()
			else:
				return HttpResponseRedirect('/appClinic/invalidForm.html')

	return HttpResponse("Lap Name "+request.POST.get("name",""))
def invalidForm(request):

	return HttpResponse("Invalid Form >>> ")