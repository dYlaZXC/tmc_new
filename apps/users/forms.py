from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from apps.users.models import User


class UserModelForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'сохранить', css_class='btn-block'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'patronymic', 'last_name', 'email']
