from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.conf import settings

def redirect_app_verify_email(request, key):
    return RedirectView.as_view(url=settings.APP_URL+'#/verify-email/'+key+"/", permanent=False)(request)


def redirect_app_reset(request, uidb64, token):
    return RedirectView.as_view(url=settings.APP_URL+'#/reset/'+uidb64+"/"+token+"/", permanent=False)(request)

urlpatterns = [
    url(r'^auth/registration/account-confirm-email/(?P<key>\w+)/$', redirect_app_verify_email, name='account_confirm_email'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', redirect_app_reset, name='password_reset_confirm'),
]
