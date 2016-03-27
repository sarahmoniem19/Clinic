from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
    url(r'^getName/$',views.getName,name="getName"),
    url(r'^your-name/$',views.yourName,name="your name"),
    url(r'^addLap/$',views.addlap,name="addlap"),
    url(r'^lapName/$',views.lapName,name="lapName")

]
