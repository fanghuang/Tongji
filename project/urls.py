from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from project import views


urlpatterns = patterns('',
	url(r'^create/$', views.ProposalCreateView.as_view(), name='create_proposal'),
	url(r'^detail/(?P<pk>[-_\d]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
	url(r'^update/(?P<pk>[-_\d]+)/$', views.ProjectUpdate.as_view(), name='project_update'),
	url(r'^search/$', views.ProjectSearchingView.as_view(), name='search_list'),
	url(r'^search/delete_post/$', views.delete_post, name="delete_post"),
	url(r'^search/update_post/$', views.update_post, name="update_post"),
)