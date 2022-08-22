from django.forms import ModelForm

from apps.organizations.models import Organization


class OrganizationModelForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'region']
