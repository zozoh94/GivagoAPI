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

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_field
from django.contrib.auth import get_user_model
import requests
import tempfile
from django.core import files

def download_file_from_url(url):
    # Stream the image from the url
    try:
        request = requests.get(url, stream=True)
    except requests.exceptions.RequestException as e:
        return None

    if request.status_code != requests.codes.ok:
        return None

    # Create a temporary file
    lf = tempfile.NamedTemporaryFile()

    # Read the streamed image in sections
    for block in request.iter_content(1024 * 8):

        # If no more file then stop
        if not block:
            break

        # Write image block to temporary file
        lf.write(block)

    return files.File(lf)

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        super(MySocialAccountAdapter,self).pre_social_login(request, sociallogin)
        email_address = sociallogin.account.extra_data['email']
        try:
            user = get_user_model().objects.get(email=email_address)
        except:
            user = None
        if user:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            sociallogin.account.user = user                                               
            sociallogin.account.save()
    def save_user(self, request, sociallogin, form=None):
        user = super(MySocialAccountAdapter, self).save_user(request, sociallogin, form)

        url = sociallogin.account.get_avatar_url()
        avatar = download_file_from_url(url)
        if avatar:            
            user.avatar.save('%s.jpg' % user.username, avatar)
        return user
    def populate_user(self, request, sociallogin, data):
        user = super(MySocialAccountAdapter, self).populate_user(request, sociallogin, data)

        if sociallogin.account.extra_data['gender'] == 'male':
            gender = get_user_model().MALE
        elif sociallogin.account.extra_data['gender'] == 'female':
            gender = get_user_model().FEMALE
        else:
            gender = None            
        user_field(user, 'gender', gender)
        
        return user
