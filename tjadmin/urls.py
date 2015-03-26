from django.conf.urls import patterns, url
from tjadmin import views


urlpatterns = patterns('',

                       url(r'^$', views.AdminView.as_view(), name="tjadmin"),
                       url(r'^login/$', views.TJAdminLoginView.as_view(), name='tjadmin_login'),
                       url(r'^create_student/$', views.CreateStudentView.as_view(), name='tjadmin_create_student'),
                       url(r'^create_student/upload/$', views.UploadStudentView.as_view(), name='tjadmin_upload_student'),
                       url(r'^create_student/upload/confirmed/$', views.UploadStudentConfirmedView.as_view(), name='tjadmin_upload_student_confirmed'),
                       )