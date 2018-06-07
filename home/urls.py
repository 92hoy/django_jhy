from django.conf.urls import url
from . import views
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
=======
>>>>>>> 813fb6ef8497c398e8d8664d487f2959a0e2720c

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^file', views.file, name='file'),
]