from django.conf.urls import patterns, url
from announcement import views


urlpatterns = patterns('',
                       url(r'^announcement/$', views.AnnouncementListView.as_view(), name='announcement_list'),

                       )