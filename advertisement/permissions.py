from rest_framework import permissions

from sponsor.models import SponsorManager

class IsManagerOfTheSponsorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the ad.
        try:
            manager_in_sponsor = obj.sponsor.managers.all()
        except SponsorManager.DoesNotExist:
            return False
        try:
            current_manager = request.user.sponsormanager
        except SponsorManager.DoesNotExist:
            return False

        return current_manager in manager_in_sponsor or request.user.is_superuser
