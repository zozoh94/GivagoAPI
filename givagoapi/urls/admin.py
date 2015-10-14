from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    url(r'^', include(admin.site.urls)),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"))
]
