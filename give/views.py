from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Count

from .serializers import GiftSerializer
from .models import Gift

class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.filter(ong__isnull=False).filter(ong__app_gift__installed=True).annotate(number_gifts=(Count('ong__ads_gift', distinct=True)+Count('ong__app_gift', distinct=True)))
    serializer_class = GiftSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
