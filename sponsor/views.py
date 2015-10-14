from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import Permission

from .serializers import SponsorSerializer
from .models import Sponsor
from .permissions import IsManagerOfTheSponsorOrReadOnly

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, IsManagerOfTheSponsorOrReadOnly)


from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.views import logout_then_login
from subdomains.utils import reverse

from advertisement.models import Ad

def sponsor_manager_check(user):
    if not user.is_authenticated():
        return False
    try:        
        sm = user.sponsormanager
    except ObjectDoesNotExist:
        return False
    try:
        sponsor = sm.sponsor
    except ObjectDoesNotExist:        
        return False

    return user.has_perms(["advertisement.add_ad", "advertisement.change_ad", "advertisement.delete_ad",
                           "sponsor.change_sponsor"])

class SponsorManagerCheckMixin(object):
    @method_decorator(user_passes_test(sponsor_manager_check))
    def dispatch(self, *args, **kwargs):
        return super(SponsorManagerCheckMixin, self).dispatch(*args, **kwargs)

def logout_view(request):
    return logout_then_login(request)

class IndexView(SponsorManagerCheckMixin, generic.View):
    def get(self, request):
        return render(request, 'sponsor/index.html') 

class AdListView(SponsorManagerCheckMixin, generic.ListView):
    model = Ad
    def get_queryset(self):
        return Ad.objects.filter(sponsor=self.request.user.sponsormanager.sponsor)

class AdDetailView(SponsorManagerCheckMixin, generic.DetailView):
    model = Ad
    def get_queryset(self):
        return Ad.objects.filter(sponsor=self.request.user.sponsormanager.sponsor)

class AdCreateView(SponsorManagerCheckMixin, generic.CreateView):
    model = Ad
    fields = ['name', 'video', 'tags']    
    def form_valid(self, form):
        form.instance.sponsor = self.request.user.sponsormanager.sponsor
        form.instance.author = self.request.user.sponsormanager
        return super(AdCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('ad-detail', 'sponsor', kwargs={'pk': self.object.id})
