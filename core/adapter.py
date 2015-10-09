from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.shortcuts import get_current_site

class MyAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        if request.is_secure():
            protocol = 'https'
        else:
            protocol = 'http'            
        current_site = get_current_site(request)
        domain = current_site.domain
        return protocol+"://"+domain+"/#/verify-email/"+emailconfirmation.key+"/"


