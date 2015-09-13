from rest_framework import viewsets
from rest_framework import permissions

from .serializers import GiftSerializer
from .models import Gift

class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
