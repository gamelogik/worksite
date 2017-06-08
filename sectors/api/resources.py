from tastypie.resources import ModelResource

from sectors.models import Cvs

class CvsResource(ModelResource):
    class Meta:
        queryset = Cvs.objects.all()
        allowed_methods = ['get']