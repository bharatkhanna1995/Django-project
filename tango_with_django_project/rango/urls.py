from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
		url(r'^$',views.index,name='index'),
        url(r'^mainpage/$',views.mainpage,name='main'),
                       url(r'^login/$', views.user_login, name='login'),)
