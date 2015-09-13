from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination

from .serializers import AdSerializer
from .serializers import AdDetailSerializer
from .models import Ad
from .permissions import IsManagerOfTheSponsorOrReadOnly
from givagoapi.paginations import CustomPagination
from sponsor.models import SponsorManager
from taggit.models import TagBase

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
        list_tags = self.request.user.interest.values_list('name', flat=True)
        if(len(list_tags) >= 6):
            ads = Ad.objects.filter(tags__name__in=list_tags).distinct()
        else:
            ads = Ad.objects.all()
        return ads
    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user.sponsormanager)
        except SponsorManager.DoesNotExist:
            raise ValidationError("You're not a Sponsor Manager")
