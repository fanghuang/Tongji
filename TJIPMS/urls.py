from django.conf.urls import patterns, include, url
from django.contrib import admin
from TJIPMS import views

urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^account/', include('account.urls')),
	url(r'^tjadmin/', include('tjadmin.urls')),
	url(r'^project/', include('project.urls')),
	url(r'^announcement/', include('announcement.urls')),
	url(r'^i18n', views.language_switch, name="language_switch"),
	url(r'^delete_post/$', views.delete_post, name="delete_post"),
)
