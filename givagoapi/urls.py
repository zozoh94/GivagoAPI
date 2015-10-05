"""givagoapi URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.views.generic.base import RedirectView

from advertisement import views as advertisement_views
from sponsor import views as sponsor_views
from give import views as give_views
from core import views as core_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ad', advertisement_views.AdViewSet)
router.register(r'sponsor', sponsor_views.SponsorViewSet)
router.register(r'gift', give_views.GiftViewSet)
router.register(r'auth/user/interest', core_views.InterestUserViewSet, base_name='interest')
router.register(r'tag', core_views.TagViewSet)

def redirect_app_verify_email(request, key):
    return RedirectView.as_view(url=settings.APP_URL+'#/verify-email/'+key+"/", permanent=False)(request)


def redirect_app_reset(request, uidb64, token):
    return RedirectView.as_view(url=settings.APP_URL+'#/reset/'+uidb64+"/"+token+"/", permanent=False)(request)

urlpatterns = [
    url(r'^auth/registration/account-confirm-email/(?P<key>\w+)/$', redirect_app_verify_email),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', redirect_app_reset),
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/facebook/$', core_views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^auth/google/$', core_views.GoogleLogin.as_view(), name='google_login'),
    url(r'^auth/linkedin/$', core_views.LinkedInLogin.as_view(), name='linkedin_login'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

