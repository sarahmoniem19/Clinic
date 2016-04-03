from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
    url(r'^getName/$',views.getName,name="getName"),
    url(r'^your-name/$',views.yourName,name="your name"),
    url(r'^addLap/$',views.addlap,name="addlap"),
    url(r'^lapName/$',views.lapName,name="lapName"),
<<<<<<< HEAD
    url(r'^invalidForm.html$',views.invalidForm,name="Invalid Form")

=======
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register")
>>>>>>> 6d39647095ba11331c4edb7ba22bee7fd2c4c4ab
]
