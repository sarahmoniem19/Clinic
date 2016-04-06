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

	#return HttpResponse("Welcome to index")
	if request.method=='POST':
		return render(request,'appClinic/loginpage.html')
	else:
		return render(request,'appClinic/home.html')

        return render(request,'appClinic/index.html')


def yourName(request):

	return HttpResponse("your name is "+request.POST.get("yourName", ""))



def addlab(request):
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


	if(request.method=='POST'):

			labForm = LabForm(request.POST)
			if labForm.is_valid():
				wtt=request.POST.get('wtt','')
				# wtt=wtt.replace('+',' ')

				wtf=request.POST.get('wtf','')
				# wtf=wtf.replace('+',' ')

				lab=labForm.save(commit=False)
				# user=myuser.objects.get(request.user.id)
				# user=myuser(pk=request.user.id)
				# user.save()
				# lab.wtf=wtf
				# lab.wtt=wtt
				# lab.owner=myuser.objects.get(request.user)
				lab.owner=myuser.objects.get(pk=1)
				lab.save()
			else:
				return HttpResponseRedirect('/appClinic/invalidForm.html')

	return HttpResponse("Lap Name "+request.POST.get("name",""))

def addHos(request):
	if(request.method=='POST'):

		hosForm = HosForm(request.POST)

		if(hosForm.is_valid):
			#create an instanse of user and pass it to labform >>
			#user=myuser()

			hosForm.save()

			return HttpResponseRedirect('/done/')

	else:
		hosForm = HosForm()
		return render(request,'appClinic/addHospital.html',{'form':hosForm})

def addCli(request):
	if(request.method=='POST'):

		cliForm = CliForm(request.POST)

		if(cliForm.is_valid):
			#create an instanse of user and pass it to labform >>
			#user=myuser()

			cliForm.save()

			return HttpResponseRedirect('/done/')

	else:
		cliForm = CliForm()
		return render(request,'appClinic/addClinic.html',{'form':cliForm})


def hosName(request):


	if(request.method=='POST'):

			hosForm = HosForm(request.POST)
			if hosForm.is_valid():
				wtt=request.POST.get('wtt','')
				# wtt=wtt.replace('+',' ')

				wtf=request.POST.get('wtf','')
				# wtf=wtf.replace('+',' ')

				hospital=hosForm.save(commit=False)
				# user=myuser.objects.get(request.user.id)
				# user=myuser(pk=request.user.id)
				# user.save()
				# lab.wtf=wtf
				# lab.wtt=wtt
				# lab.owner=myuser.objects.get(request.user)
				hospital.owner=myuser.objects.get(pk=1)
				hospital.save()
			else:
				return HttpResponseRedirect('/appClinic/invalidForm.html')

	return HttpResponse("Lap Name "+request.POST.get("name",""))

def cliName(request):


	if(request.method=='POST'):

			cliForm = LabForm(request.POST)
			if cliForm.is_valid():
				wtt=request.POST.get('wtt','')
				# wtt=wtt.replace('+',' ')

				wtf=request.POST.get('wtf','')
				# wtf=wtf.replace('+',' ')

				clinic=cliForm.save(commit=False)
				# user=myuser.objects.get(request.user.id)
				# user=myuser(pk=request.user.id)
				# user.save()
				# lab.wtf=wtf
				# lab.wtt=wtt
				# lab.owner=myuser.objects.get(request.user)
				clinic.owner=myuser.objects.get(pk=1)
				clinic.save()
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
	result_lab =labAnalysis.objects.all()
	spec_clinic =clinic.objects.all()
	loc_hospital=hospital.objects.all()
	loc_lab=lab.objects.all()
	if 'data' in request.GET:
		value = request.GET['data']
		query_clinic = clinic.objects.filter (name__icontains =  value) 
		query_lab = lab.objects.filter (name__icontains = value)
		query_hospital = hospital.objects.filter (name__icontains = value)
		return render(request,'appClinic/search.html',{'query_clinic':query_clinic,'query_lab':query_lab,'query_hospital':query_hospital,'result_lab':result_lab,'spec_clinic':spec_clinic,'loc_hospital':loc_hospital,'loc_lab':loc_lab})
		
def search_simple(request):
	return render (request,'appClinic/search_simple.html')
	
def result(request):
	if 'type' in request.GET:	
		search = request.GET['type']
		if search == "Clinics":
			if 'location' in request.GET:
				loca = request.GET['location']
			if 'spec' in request.GET:
				spec = request.GET['spec']
			if 'price' in request.GET:
				cost = request.GET['price']
				if cost == '2':
					#results = clinic.objects.get ( Q(cost__lt = 300) & Q(cost__gte = 100) & Q(city__icontains = loc) & Q(cSpec__icontains = spec) ) 
					results = clinic.objects.filter (price__range=(100, 300) , city__icontains = loca , cSpec__icontains = spec) 
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic })
				elif cost == '1':	
					results = clinic.objects.all().filter (city__icontains = loca , cSpec__icontains = spec , price__lte = 100)
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})
				elif cost == '3':	
					#results = clinic.objects.filter (city__icontains = loc , cSpec__icontains = spec , cost__lte = 500 , cost__gte = 300)
					results = clinic.objects.filter (price__range=(300, 500) , city__icontains = loca , cSpec__icontains = spec) 
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})	
				elif cost == '4':	
					results = clinic.objects.filter (city__icontains = loca , cSpec__icontains = spec , price__gt = 500)
					return render (request, 'appClinic/result.html' , {'results':results , "type": clinic})
		if search == "Hospitals":
			if 'location' in request.GET:
				loca = request.GET['location']
			if 'level' in request.GET:
				le = request.GET['level']
				results = hospital.objects.filter (city__icontains = loca , level__icontains = le)
				return render (request, 'appClinic/result.html' , {'results':results , "type": hospital })	 	
		if search == "Labs":	
			if 'location' in request.GET:
				loca = request.GET['location']
			if 'level' in request.GET:
				le = request.GET['level']	
				results = lab.objects.filter (city__icontains = loca , level__icontains = le)
				return render (request, 'appClinic/result.html' , {'results':results,"type": lab}) 
			if 'lab_analysis' in request.GET:

				lab_analysis = request.GET('lab_analysis')
				le = request.GET['lab_analysis']	
				results = lab.objects.filter (city__icontains = loca , level__icontains = le , type__icontains = lab_analysis)
				return render (request, 'appClinic/result.html' , {'request':request , "type": lab})
			#select labanalfrom labanyl,lab where labaylid=labid and labowner=1

def itemprofile(request):
	type = request.GET['name']
	item_id = request.GET['id']
	if type=='clinic':
		q = clinic
		query = q.objects.all().get(id=item_id)
	elif type=='hospital':
		q = hospital
		query = q.objects.all().get(id=item_id)
	else:
		q = lab
		q2 = labAnalysis
		query = q.objects.all().get(id=item_id)
		lab_anal_q = q2.objects.all().filter(labId_id=item_id)
		return render(request,'appClinic/itempage.html',{'result':query,'type':type,'lab':lab_anal_q})
	return render(request,'appClinic/itempage.html',{'result':query,'type':type})
		

def listitems(request):
	#user = request.user
	c=clinic
	h=hospital
	l=lab
	user =1
	clin = c.objects.all().filter(owner_id=1)
	hos = h.objects.all().filter(owner_id=1)
	labs = l.objects.all().filter(owner_id=1)
	q2 = labAnalysis
	#lab_anal_q = q2.objects.all().filter(labId=labs)
	return render(request,'appClinic/list_adds_business.html',{'hospitals':hos,'labs':labs,'clinics':clin})

def edititem(request):
	type = request.GET['type']
	item_id = request.GET['id']
	if type=='clinic':
		q = clinic
		query = q.objects.all().get(id=item_id)
	elif type=='hospital':
		q = hospital
		query = q.objects.all().get(id=item_id)
	else:
		q = lab
		q2 = labAnalysis
		query = q.objects.all().get(id=item_id)
		lab_anal_q = q2.objects.all().filter(labId_id=item_id)
		return render(request,'appClinic/edititem.html',{'result':query,'type':type,'lab':lab_anal_q})
	return render(request,'appClinic/edititem.html',{'result':query,'type':type})

def update(request):
	type = request.GET['type']
	if type=='hospital':
		form = request.POST
		h=hospital.objects.all().get(id=form['id'])
		h.name = form['name']
		h.logo = form['logo']
		h.wtt = form['wtt']
		h.wtf = form['wtf']
		h.country = form['country']
		h.city = form['city']
		h.region = form['region']
		h.notes = form['notes']
		h.phone = form['phone']
		h.save()
		return HttpResponse('done')
	elif type=='clinic':
		form = request.POST
		h=clinic.objects.all().get(id=form['id'])
		h.name = form['name']
		h.logo = form['logo']
		h.wtt = form['wtt']
		h.wtf = form['wtf']
		h.country = form['country']
		h.city = form['city']
		h.region = form['region']
		h.notes = form['notes']
		h.phone = form['phone']
		h.dname = form['dname']
		h.dQlfy = form['dQlfy']
		h.cSpec = form['cSpec']
		h.price = form['price']
		h.save()
		return HttpResponse('done')
	else:
		form = request.POST
		h=lab.objects.all().get(id=form['id'])
		h.name = form['name']
		h.logo = form['logo']
		h.wtt = form['wtt']
		h.wtf = form['wtf']
		h.country = form['country']
		h.city = form['city']
		h.region = form['region']
		h.notes = form['notes']
		h.phone = form['phone']
		h.save()
		return HttpResponse('done')

def update_anal(request):
	rid = request.GET['id']
	labobj = labAnalysis.objects.all().get(id=rid)
	if request.method == 'POST':
		labobj.type = request.POST['type']
		labobj.price = request.POST['price']
		labobj.save()
		return HttpResponse('/done')
	else:
		return render(request,'appClinic/editlabanal.html',{'lobj':labobj})

def delitem(request):
	type = request.GET['type']
	itemid = request.GET['id']
	if type=='clinic':
		clinic.objects.all().get(id=itemid).delete()
		return HttpResponse('/del')
	elif type=='hospital':
		hospital.objects.all().get(id=itemid).delete()
		return HttpResponse('/del')
	else:
		la = lab.objects.all().get(id=itemid)
		labAnalysis.objects.all().filter(labId=la).delete()
		la.delete()
		return HttpResponse('/del')

def del_anal(request):
	analid = request.GET['id']
	labAnalysis.objects.all().get(id=analid).delete()
	return HttpResponse('/del')

"""la = request.GET['lab_analysis']
				#get all labAnalysis
				labAna = labAnalysis.objects.all()
				#get FK ID
				labAnaID = labAna.labId_id
				#get required ((labs))
				labsList = lab.objects.filter (city__icontains = loca , level__icontains = le)
				#get where lab ID = labanalysis ID FK
				#get all labs in loca & le & type in labAnalysis = la 
				results=lab.objects.get( id=labAnaID)	
					
				return render (request, 'appClinic/result.html' , {'results':results,"type": lab}) 
 
<<<<<<< HEAD


def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)"""

=======
>>>>>>> ca777895de0360d554bf1ef9da49fe401553defc
