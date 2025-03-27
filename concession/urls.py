from django.urls import path
from . import views_auth
from . import views
urlpatterns = [
  path("", views.login, name="login"),
  path("home/", views.homepage, name="home"),
  path("concession/", views.myform, name="concession"),
  path("myadmin/", views.myadmin, name="myadmin"),
  path("status/", views.settings, name="mysettings"),
  path("settings/", views.status, name="status"),
  path("logout/",views.logout,name="logout"),
  path("savedata/",views_auth.savedata,name="savedata"),#SignUp Url
  path("savedetails/",views_auth.savedetail,name="savedetail"),# Candidate details URL
  path("login_ajax/", views_auth.login_ajax, name="login_ajax"),
  # path("con_page/",views_auth.railway_concession_form,name="concessionform")
  
]