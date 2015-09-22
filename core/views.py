from rest_framework import viewsets
from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class InterestUserViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'name'
    def get_queryset(self):
        return self.request.user.interest
    def list(self, request):
        interests = request.user.interest.names()
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
        tags = Tag.objects.filter(name__icontains=query).values_list('name', flat=True)
        return Response(tags)
