from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django.core.exceptions import ValidationError
from django.forms import ModelForm, RadioSelect, Form, DateField, DateInput, SelectMultiple
from django.forms.widgets import Select

from apps.common.form_helpers import HorizontalFormHelper
from apps.crm.models import ClientCall, Complaint, Client, Consultation


class ClientModelForm(ModelForm):
    helper = HorizontalFormHelper()
    helper.form_tag = False

    class Meta:
        model = Client
        fields = ['phone', 'last_name', 'first_name', 'patronymic', 'iin']


class ClientCallModelForm(ModelForm):
    helper = HorizontalFormHelper()
    helper.form_tag = False

    class Meta:
        model = ClientCall
        fields = ('kind', 'region', 'organization', 'text', 'answer')
        widgets = {
            'kind': RadioSelect,
            'organization': Select(attrs={'class': 'js-select2'}),
        }


class ComplaintModelForm(ModelForm):
    helper = HorizontalFormHelper()
    helper.form_tag = False

    class Meta:
        model = Complaint
        fields = ('topics',)
        widgets = {
            'topics': SelectMultiple(attrs={'class': 'js-select2'}),
        }


class ComplaintUpdateModelForm(ModelForm):
    helper = HorizontalFormHelper()
    helper.form_tag = False

    class Meta:
        model = Complaint
        fields = ('status', 'actions', 'result')
        widgets = {
            'result': RadioSelect,
        }


class ConsultationModelForm(ModelForm):
    helper = HorizontalFormHelper()
    helper.form_tag = False

    class Meta:
        model = Consultation
        fields = ('category', 'article')


class ReportForm(Form):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Div('start_date', css_class='col-sm-4'),
            Div('end_date', css_class='col-sm-4'),
            Div(
                Div(
                    Submit('submit', 'выгрузить', css_class='btn-block'),
                    css_class='form-group'),
                css_class='col-sm-4 d-flex align-self-end'),
            css_class='form-row'
        )
    )
    start_date = DateField(label='начало периода', widget=DateInput(attrs={'class': 'js-date-input'}))
    end_date = DateField(label='конец периода', widget=DateInput(attrs={'class': 'js-date-input'}))

    def clean(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            raise ValidationError('начальная дата должна быть раньше чем конечная')
