"""givagoapi URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings

from advertisement import views as advertisement_views
from sponsor import views as sponsor_views
from give import views as give_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ad', advertisement_views.AdViewSet)
router.register(r'sponsor', sponsor_views.SponsorViewSet)
router.register(r'gift', give_views.GiftViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
