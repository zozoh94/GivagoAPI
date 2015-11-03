from rest_framework import viewsets
from taggit.models import Tag
from taggit_suggest.utils import suggest_tags
from taggit_serializer.serializers import TaggitSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.linkedin.views import LinkedInOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework import serializers

class SocialLoginMixin(object):
    def initialize_request(self, request, *args, **kwargs):
        request =  super(SocialLoginMixin, self).initialize_request(request, *args, **kwargs)
        self.callback_url = request.data['redirectUri']
        return request

class FacebookLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client   
class GoogleLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client   
class LinkedInLogin(SocialLoginMixin, SocialLoginView):
    adapter_class = LinkedInOAuthAdapter
    client_class = OAuth2Client
  
class InterestUserViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'name'
    serializer_class = serializers.Serializer
    def get_queryset(self):
        return self.request.user.interest
    def list(self, request):
        interests = request.user.interests()
        return Response(interests)
    def create(self, request):
        try:
            tags = request.data['tags']
        except:
            tags = None
        if tags is None:
            return Response({'detail' : 'Please specify one or many tags.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.interest.add(tags)
        return Response({'status' : 'ok'})
    def destroy(self, request, name=None):
        tag = name;
        if tag is None:
            return Response({'detail' : 'Please specify one tag.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.interest.remove(tag)
        return Response({'status' : 'ok'})

class TagViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    lookup_field = 'name'
    queryset = Tag.objects.all()
    def list(self, request):
        try:
            query = request.query_params['query']
        except:
            return Response(Tag.objects.values_list('name', flat=True))
        tags = suggest_tags(query)
        return Response(tags)

from rest_framework.views import APIView
from .serializers import CharityContactFormSerializer
from .serializers import SponsorContactFormSerializer
from .serializers import CommunityContactFormSerializer
from django.core.mail import BadHeaderError
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage

class ContactFormView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data        
            to = [settings.DEFAULT_CONTACT_EMAIL]
            from_email = settings.DEFAULT_FROM_EMAIL
            try:
                message = get_template(self.template).render(Context(data))
                msg = EmailMessage(self.subject, message, to=to, from_email=from_email, reply_to=[data['email']])
                msg.content_subtype = 'html'
                msg.send()
            except BadHeaderError:
                return Response({'detail' : 'Header incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status' : 'ok'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CharityContactFormView(ContactFormView):
    serializer_class = CharityContactFormSerializer
    subject = "Charity contact"
    template = 'email/charity.html'   

class SponsorContactFormView(ContactFormView):
    serializer_class = SponsorContactFormSerializer
    subject = "Sponsor contact"
    template = 'email/message.html'

class CommunityContactFormView(ContactFormView):
    serializer_class = CommunityContactFormSerializer
    subject = "Community contact"
    template = 'email/community.html'
