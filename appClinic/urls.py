from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
    url(r'^getName/$',views.getName,name="getName"),
    url(r'^your-name/$',views.yourName,name="yourname"),
    url(r'^addLab/$',views.addlab,name="addlab"),
    url(r'^addHos/$',views.addHos,name="addHos"),
    url(r'^addCli/$',views.addCli,name="addClinic"),
    url(r'^lapName/$',views.lapName,name="lapName"),
    url(r'^invalidForm.html$',views.invalidForm,name="InvalidForm"),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),

    url(r'^search/', views.search),
	url(r'^result/', views.result),
	url(r'^search_simple/', views.search_simple),
    url(r'^list_additem/',views.listitems),
    url(r'^edit_item/',views.edititem),
    url(r'^update/',views.update),
    url(r'update_anal/',views.update_anal),
    url(r'del/',views.delitem),
    url(r'del_anal/',views.del_anal),

    url(r'^search/', views.search, name="search"),
	url(r'^result/', views.result, name="result"),
	url(r'^search_simple/', views.search_simple, name="search_simple"),

]
