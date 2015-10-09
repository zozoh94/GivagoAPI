from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings

from advertisement import views as advertisement_views
from sponsor import views as sponsor_views
from give import views as give_views
from core import views as core_views

from givagoapi.urls.sponsor import urlpatterns as sponsor_urls

router = routers.DefaultRouter()
router.register(r'ad', advertisement_views.AdViewSet)
router.register(r'sponsor', sponsor_views.SponsorViewSet)
router.register(r'gift', give_views.GiftViewSet)
router.register(r'auth/user/interest', core_views.InterestUserViewSet, base_name='interest')
router.register(r'tag', core_views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/facebook/$', core_views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^auth/google/$', core_views.GoogleLogin.as_view(), name='google_login'),
    url(r'^auth/linkedin/$', core_views.LinkedInLogin.as_view(), name='linkedin_login'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
    urlpatterns.append(url(r'^sponsor/', include(sponsor_urls)))
