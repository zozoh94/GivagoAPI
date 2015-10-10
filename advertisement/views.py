from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status

from .serializers import AdSerializer
from .serializers import AdDetailSerializer
from .models import Ad
from .models import View
from give.models import Gift
from .permissions import IsManagerOfTheSponsorOrReadOnly
from givagoapi.paginations import CustomPagination
from sponsor.models import SponsorManager
from django_random_queryset import RandomManager

#class AdsPagination(CustomPagination):
#    page_size = 4
    
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, IsManagerOfTheSponsorOrReadOnly)
    #pagination_class = AdsPagination
    def retrieve(self, request, pk=None):
        self.serializer_class = AdDetailSerializer
        return super(AdViewSet, self).retrieve(request, pk)
    def get_queryset(self):
        if(self.request.user.is_anonymous()):
            return Ad.objects.filter(remaining_views__gt=0).random(4)
        list_tags = self.request.user.interest.values_list('name', flat=True)
        ads = Ad.objects.filter(remaining_views__gt=0).filter(tags__name__in=list_tags).exclude(views__viewer__id=self.request.user.id).distinct()
        if(len(ads) < 4):
            ads = Ad.objects.filter(remaining_views__gt=0)
        return ads.random(4)
    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user.sponsormanager)
        except SponsorManager.DoesNotExist:
            raise ValidationError("You're not a Sponsor Manager")
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def see(self, request, pk=None):
        view = View()
        view.ad = self.get_object()
        view.viewer = request.user
        try:
            give = request.data['give']
        except:
            return Response({'detail' : 'Please specify give parameter.'}, status=status.HTTP_400_BAD_REQUEST)
        view.ong = Gift.objects.get(id=give).ong        
        view.save()
        if view.ad.id in request.user.ads_viewed.values_list('ad', flat=True):
            return Response({'status': 'already see'})        
        return Response({'status': 'ok'})
    
