from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from django.forms import ModelForm
from .forms import *

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
        return render(request,'appClinic/index.html')

def yourName(request):

	return HttpResponse("your name is "+request.POST.get("yourName", ""))


def addlap(request):
	if(request.method=='POST'):
		labForm = LabForm(request.POST)

		if(labForm.is_valid):
			#create an instanse of user and pass it to labform >>
			#user=myuser()

			labForm.save()

			return HttpResponseRedirect('/done/')

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

def login(request):
	if(request.method=='POST'):
		p=User
		form = request.POST
		usern=form['username']
		passwrd=form['password']
		user = authenticate(username=usern , password=passwrd)
		if user is not None:
			# the password verified for the user
			return render(request, 'appClinic/index.html')
			##after redirect to page get user object by (request.user)
		else:
			# the authentication system was unable to verify the username and password
			return HttpResponse("The username and password were incorrect.")

	else:
		return render(request,'appClinic/loginpage.html')

def register(request):
	if(request.method=='POST'):
		p=User()
		form=request.POST
		p.first_name=form['first_name']
		p.last_name=form['last_name']
		p.username=form['username']
		p.email=form['email']
		p.set_password(form['password'])
		p.save()
		p2=myuser()
		p2.user_id = User.objects.get_by_natural_key(form['username']).id
		p2.dob = form['dob']
		p2.city = form['city']
		p2.country = form['country']
		p2.region = form['region']
		p2.gender = form['gender']
		p2.accType = form['accType']
		p2.save()
		return  HttpResponse("succeded")
	else:
		reg = registerForm
		reg2 = registerf
		return render(request,'appClinic/register.html',{'form':reg,'form2':reg2})
    
def search (request):
    if 'data' in request.GET:
        value = request.GET['data']
        query_clinic = clinic.objects.filter (name__icontains =  value) 
        query_lab = lab.objects.filter (name__icontains = value)
        query_hospital = hospital.objects.filter (name__icontains = value)
        return render(request,'appClinic/search.html',{'query_clinic':query_clinic ,'query_lab':query_lab,'query_hospital':query_hospital})
    else:
        return render (request, 'appClinic/search_simple.html')	 		 	 	

    
	

def search_simple(request):
	return render (request,'appClinic/search_simple.html')
	
def result(request):
	if 'type' in request.GET:	
		search = request.GET['type']
		if search == "Clinics":
			if 'location' in request.GET:
				loc = request.GET['location']
			if 'spec' in request.GET:
				spec = request.GET['spec']
			if 'price' in request.GET:
				cost = request.GET['price']
				if cost == '2':
					#results = clinic.objects.get ( Q(cost__lt = 300) & Q(cost__gte = 100) & Q(city__icontains = loc) & Q(cSpec__icontains = spec) ) 
					results = clinic.objects.filter (price__range=(100, 300) , city__icontains = loc , cSpec__icontains = spec) 
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})
				elif cost == '1':	
					results = clinic.objects.all().filter (city__icontains = loc , cSpec__icontains = spec , price__lte = 100)
					return render (request, 'appClinic/result.html' , {'results':results})
				elif cost == '3':	
					#results = clinic.objects.filter (city__icontains = loc , cSpec__icontains = spec , cost__lte = 500 , cost__gte = 300)
					results = clinic.objects.filter (price__range=(300, 500) , city__icontains = loc , cSpec__icontains = spec) 
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})	
				elif cost == '4':	
					results = clinic.objects.filter (city__icontains = loc , cSpec__icontains = spec , price__gt = 500)
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})
		elif search == "Hospitals":
			if 'location' in request.GET:
				loc = request.GET['location']
			if 'level' in request.GET:
				le = request.GET['level']
				results = hospital.objects.filter (city__icontains = loc , level__icontains = le)
				return render (request, 'appClinic/result.html' , {'request':request , "type": hospital})	 	
		elif search == "Labs":	
			if 'location' in request.GET:
				loc = request.GET['location']
			if 'level' in request.GET:
				le = request.GET['level']
			if 'lab_analysis' in request.GET:
				le = request.GET['lab_analysis']	
				results = lab.objects.filter (city__icontains = loc , level__icontains = le , type__icontains = lab_analysis)
				return render (request, 'appClinic/result.html' , {'request':request , "type": lab})	 		 	 	
		

