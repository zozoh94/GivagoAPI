from rest_framework import viewsets
from rest_framework import permissions

from .serializers import SponsorSerializer
from .models import Sponsor

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )