from django.forms import ModelForm

from apps.geo.models import Region


class RegionModelForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name']
