from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import AdSerializer
from .serializers import AdDetailSerializer
from .models import Ad
from .permissions import IsManagerOfTheSponsorOrReadOnly
from givagoapi.paginations import CustomPagination
from sponsor.models import SponsorManager
from taggit.models import TagBase
from django_random_queryset import RandomManager

class AdsPagination(CustomPagination):
    page_size = 6
    
# Create your views here.
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, IsManagerOfTheSponsorOrReadOnly)
    pagination_class = AdsPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = AdDetailSerializer
        return super(AdViewSet, self).retrieve(request, pk)
    def get_queryset(self):
        if(self.request.user.is_anonymous()):
            ads =  Ad.objects.all()
            return ads.random(30)
        list_tags = self.request.user.interest.values_list('name', flat=True)
        ads = Ad.objects.filter(tags__name__in=list_tags).exclude(viewer__id=self.request.user.id).distinct()
        if(len(ads) < 1):
            ads = Ad.objects.all()
        return ads.random(30)
    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user.sponsormanager)
        except SponsorManager.DoesNotExist:
            raise ValidationError("You're not a Sponsor Manager")
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def see(self, request, pk=None):
        ad = self.get_object()
        #if Ad.objects.filter(viewer__id=request.user.id).exists() :
        if ad.id in request.user.ads_viewed.values_list('id', flat=True):
            return Response({'status': 'already see'})
        request.user.ads_viewed.add(ad)
        request.user.save()
        return Response({'status': 'ok'})
    
