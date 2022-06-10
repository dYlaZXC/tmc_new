from crispy_forms.helper import FormHelper


class HorizontalFormHelper(FormHelper):
    wrapper_class = 'row'
    form_group_wrapper_class = 'row'
    label_class = 'col-3'
    field_class = 'col-9'

    def __init__(self):
        super().__init__()
        self.wrapper_class = 'row'
