from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import pagination
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError, transaction
from django.db.models import Q, Count
from datetime import datetime
from django.conf import settings
from ipware.ip import get_ip
from django.contrib.gis.geoip import GeoIP

from .serializers import AdSerializer
from .serializers import AdDetailSerializer
from .serializers import AppSerializer
from .models import Ad
from .models import View
from .models import App
from .models import AppClick
from give.models import Gift
from .permissions import IsManagerOfTheSponsorOrReadOnly
from sponsor.models import SponsorManager

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, IsManagerOfTheSponsorOrReadOnly)
    def retrieve(self, request, pk=None):
        self.serializer_class = AdDetailSerializer
        self.queryset = Ad.objects.all().annotate(number_views=Count('views')).annotate(number_views_different_user=Count('views__viewer', distinct=True))
        return super(AdViewSet, self).retrieve(request, pk)
    def get_queryset(self):
        if(self.request.user.is_anonymous()):
            return Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1)).order_by('?')
        list_tags = self.request.user.interest.values_list('name', flat=True)
        ads = Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1)).filter(tags__name__in=list_tags).exclude(views__viewer__id=self.request.user.id).distinct()
        if(len(ads) < 4):
            ads = Ad.objects.filter(Q(remaining_views__gt=0) | Q(remaining_views=-1))
        return ads.order_by('?')
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
                view.ong = Gift.objects.get(name=give).ong
                ad.save()
                view.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if ad.id in request.user.ads_viewed.values_list('ad', flat=True):
            return Response({'status': 'already see'})        
        return Response({'status': 'ok'})
    @list_route(methods=['post'], permission_classes=[permissions.IsAuthenticated], url_path='see/dailymotion')
    def see_dailymotion(self, request):
        try:
            give = request.data['give']
        except:
            return Response({'detail' : 'Please specify give parameter.'}, status=status.HTTP_400_BAD_REQUEST)
        try:        
            view = View()
            view.type = View.DAILYMOTION_TYPE
            view.viewer = request.user
            view.ong = Gift.objects.get(name=give).ong
            view.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'status': 'ok'})

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    def list(self, request):
        ip = get_ip(request)
        g = GeoIP()
        country = g.country(ip)

        if country['country_code'] not in settings.ALLOWED_COUNTRIES and ip != '127.0.0.1':
            return Response({'detail' : 'Applications for this country are unvailable. Country detected : '+country['country_name']}, status=status.HTTP_403_FORBIDDEN)
        
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

        apps_free = App.objects.filter(os=App.FREEAPP_OS).order_by('-rpa')
        if os_found == App.ANDROIDAPP_OS:
            apps = App.objects.filter(os=App.ANDROIDAPP_OS).order_by('-rpa')
        elif os_found == App.IPADAPP_OS:
            apps = App.objects.filter(Q(os=App.IPADAPP_OS) | Q(os=App.IOSAPP_OS)).order_by('-rpa')
        elif os_found == App.IPHONEAPP_OS:
            apps = App.objects.filter(Q(os=App.IPHONEAPP_OS) | Q(os=App.IOSAPP_OS)).order_by('-rpa')
        elif os_found == App.IOSAPP_OS:
            apps = App.objects.filter(os=App.IOSAPP_OS).order_by('-rpa')
        else:
            apps = None
        if apps == None:
            apps = apps_free
        else:
            list(apps)
            for q in apps_free:
                apps._result_cache.append(q)

        if request.user.is_authenticated():
            app_clicked_installed = AppClick.objects.filter(viewer=request.user).filter(installed=True).exclude(app=None)
            apps = apps.exclude(clicks=app_clicked_installed)
 
        serializer = self.get_serializer(apps, many=True)
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
        app_click.ong = Gift.objects.get(name=give).ong
        try:
            app_click.save()
        except IntegrityError:
            return  Response({'detail' : 'Problem with the database.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({'cid': app_click.id})

from django.views.decorators.http import require_GET
from django.http import Http404, HttpResponseServerError, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


@require_GET
def app_installed_view(request, cid):
    try:
        app_click = AppClick.objects.get(id=cid)
    except AppClick.DoesNotExist:
        return Http404('App click does not exist.')
        
    app_click.installed = True    
    app_click.date_installed = datetime.now()
    try:
        app_click.save()
    except IntegrityError:
        return  HttpResponseServerError('Problem with the database.')
    
    return HttpResponse('ok')

@require_GET
def app_click_view(request, give_name, app_id, username):
    try:
        give = Gift.objects.get(name=give_name)
    except Gift.DoesNotExist:
        raise Http404("Gift does not exist")
    try:
        app = App.objects.get(pk=app_id)
    except App.DoesNotExist:
        raise Http404("App does not exist")
    try:
        user = get_user_model().objects.get(username=username)
    except get_user_model().DoesNotExist:
        raise Http404("User does not exist")
    
    
    app_click = AppClick()
    app_click.app = app
    app_click.viewer = user
    app_click.ong = give.ong
    try:
        app_click.save()
    except IntegrityError:
        return  HttpResponseServerError('Problem with the database.')

    app_link = app.link
    app_link = app_link.replace('{cid}', str(app_click.id))
    app_link = app_link.replace('{username}', username)
    app_link = app_link.replace('{interests}', str(user.interest.values_list('name', flat=True)))
    app_link = app_link.replace('{give}', give_name)
    app_link = app_link.replace('{gender}', dict(get_user_model().GENDER_CHOICES)[user.gender] if user.gender else '')
    app_link = app_link.replace('{date_birth}', str(user.date_birth) if user.date_birth else '')
    app_link = app_link.replace('{income_level}', dict(get_user_model().INCOME_LEVEL_CHOICES)[user.income_level] if user.income_level else '')

    return redirect(app_link)
