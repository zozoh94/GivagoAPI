from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.http import HttpResponse

from advertisement import views as advertisement_views
from sponsor import views as sponsor_views
from give import views as give_views
from core import views as core_views
from actfund import views as actfund_views

router = routers.DefaultRouter()
router.register(r'ad', advertisement_views.AdViewSet)
router.register(r'sponsor', sponsor_views.SponsorViewSet)
router.register(r'gift', give_views.GiftViewSet)
router.register(r'auth/user/interest', core_views.InterestUserViewSet, base_name='interest')
router.register(r'tag', core_views.TagViewSet)
router.register(r'app', advertisement_views.AppViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/registration/verify-email/login/$', core_views.VerifyEmailLoginAutoView.as_view(), name='rest_verify_email_login_auto'),
    url(r'^app/installed/(?P<cid>[a-z0-9-]+)/$', advertisement_views.app_installed_view), 
    url(r'^app/(?P<app_id>\d+)/click/(?P<give_name>[\w_-]+)/(?P<username>[\w@.+_-]+)/$', advertisement_views.app_click_view),
    url(r'^actfund/survey/completed', actfund_views.survey_completed_view),
    url(r'^actfund/survey/total', actfund_views.survey_total_amount_view),
    url(r'^contact/charity', core_views.CharityContactFormView.as_view()),
    url(r'^contact/sponsor', core_views.SponsorContactFormView.as_view()),
    url(r'^contact/community', core_views.CommunityContactFormView.as_view()),
    url(r'^auth/facebook/$', core_views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^auth/google/$', core_views.GoogleLogin.as_view(), name='google_login'),
    url(r'^auth/linkedin/$', core_views.LinkedInLogin.as_view(), name='linkedin_login'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
