from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from account import views


urlpatterns = patterns('',
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
	url(r'^profile/$', views.ProfileView.as_view(success_url=reverse_lazy('index')), name='profile'),
	url(r'^setting/$', views.SettingView.as_view(), name='setting'),
)