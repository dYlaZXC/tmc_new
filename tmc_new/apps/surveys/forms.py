from crispy_forms.helper import FormHelper
from django.forms import ModelForm, HiddenInput, inlineformset_factory, RadioSelect

from apps.surveys.models import Answer, Interview


class AnswerModelForm(ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Answer
        fields = ('question', 'choice')
        widgets = {
            'question': HiddenInput,
            'choice': RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = self.initial['question'].choices.all()
        self.fields['choice'].label = self.initial['question'].text


AnswersFormset = inlineformset_factory(Interview, Answer, form=AnswerModelForm, can_delete=False, extra=3)
