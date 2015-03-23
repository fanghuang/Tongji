from django.conf.urls import patterns, url
from tjadmin import views


urlpatterns = patterns('',

                       url(r'^$', views.AdminView.as_view(), name="tjadmin"),
                       url(r'^login/$', views.LoginView.as_view(), name='tjadmin_login'),
                       url(r'^create_student/$', views.CreateStudentView.as_view(), name='tjadmin_create_student'),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
                       )