from django.conf.urls import include, url
from django.http import HttpResponse

from sponsor import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url('^logout/$', views.logout_view, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^ad/$', views.AdListView.as_view(), name='ad-list'),
    url(r'^ad/(?P<pk>[0-9]+)/$', views.AdDetailView.as_view(), name='ad-detail'),
    url(r'^ad/add/$', views.AdCreateView.as_view(), name='ad-add')
]
