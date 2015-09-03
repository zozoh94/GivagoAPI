from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination

from .serializers import AdSerializer
from .models import Ad
from .permissions import IsManagerOfTheSponsorOrReadOnly
from givagoapi.paginations import CustomPagination
from sponsor.models import SponsorManager

class AdsPagination(CustomPagination):
    page_size = 6
    
# Create your views here.
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, IsManagerOfTheSponsorOrReadOnly)
    pagination_class = AdsPagination
    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user.sponsormanager)
        except SponsorManager.DoesNotExist:
            raise ValidationError("You're not a Sponsor Manager")

