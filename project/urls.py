from django.conf.urls import patterns, url
from project import views


urlpatterns = patterns('',
                       url(r'^create/$', views.ProposalCreateView.as_view(), name='create_proposal'),
                       url(r'^detail/(?P<pk>[-_\d]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
                       )