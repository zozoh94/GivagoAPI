from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from django.db.models import Q
from datetime import datetime

from .serializers import AdSerializer
from .serializers import AdDetailSerializer
from .serializers import AppSerializer
from .models import Ad
from .models import View
from .models import App
from .models import AppClick
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
            return Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1)).random(4)
        list_tags = self.request.user.interest.values_list('name', flat=True)
        ads = Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1)).filter(tags__name__in=list_tags).exclude(views__viewer__id=self.request.user.id).distinct()
        if(len(ads) < 4):
            ads = Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1))
        return ads.random(4)
    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user.sponsormanager)
        except SponsorManager.DoesNotExist:
            raise ValidationError("You're not a Sponsor Manager")
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def see(self, request, pk=None):        
        ad = self.get_object()
        try:
            give = request.data['give']
        except:
            return Response({'detail' : 'Please specify give parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                if ad.remaining_views > 0:
                    ad.remaining_views -= 1
                view = View()
                view.ad = ad
                view.type = View.AD_TYPE
                view.viewer = request.user
                view.ong = Gift.objects.get(id=give).ong
                ad.save()
                view.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if ad.id in request.user.ads_viewed.values_list('ad', flat=True):
            return Response({'status': 'already see'})        
        return Response({'status': 'ok'})
    
class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    def list(self, request):
        try:
            os = request.query_params['os']
        except:
            return Response({'detail' : 'Please specify os parameter.'}, status=status.HTTP_400_BAD_REQUEST)
        os_found = None
        for item in App.OS_CHOICES:
            if os in item:
                os_found = item[0]
                break
        if os_found == None:   
            return Response({'detail' : 'Please specify a correct os parameter.'}, status=status.HTTP_400_BAD_REQUEST)
        random_app = App.objects.filter(os=os_found).random(1).first()
        serializer = self.get_serializer(random_app, many=False)
        return Response(serializer.data)
    @detail_route(methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def click(self, request, pk=None):        
        app = self.get_object()
        try:
            give = request.data['give']
        except:
            return Response({'detail' : 'Please specify give parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        app_click = AppClick()
        app_click.app = app
        app_click.viewer = request.user
        app_click.ong = Gift.objects.get(id=give).ong
        try:
            app_click.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'clickId': app_click.id})
    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def installed(self, request):
        try:
            app_click_id = request.data['clickId']
        except:
            return Response({'detail' : 'Please specify clickId parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        app_click = AppClick.objects.get(id=app_click_id)
        app_click.installed = True
        app_click.date_installed = datetime.now()
        try:
            app_click.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'status': 'ok'})
