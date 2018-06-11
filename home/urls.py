from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from home.views import Post

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^file', views.file, name='file'),
    url(r'^post_insert', views.post_insert, name='post_insert'),
    url(r'^post_list_data$', views.post_list_data, name='post_list_data'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post_ud$', views.post_ud, name='post_ud'),
]