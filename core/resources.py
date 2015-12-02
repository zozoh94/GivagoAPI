from import_export import resources
from django.contrib.auth import get_user_model

class UserResource(resources.ModelResource):

    class Meta:
        model = get_user_model()
        fields = ('username', 'firstname', 'last_name', 'email')
