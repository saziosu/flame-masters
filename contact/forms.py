from django.forms import ModelForm
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Reset


class ContactForm(ModelForm):
    """
    A modelform from the Contact model
    For the user to enter their queries
    """
    class Meta:
        model = Contact
        fields = [
            'reason',
            'order_number',
            'name',
            'email',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        # crispy forms helper and layouts
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'contactform'
        self.helper.layout = Layout(
            Field('reason'),
            Field('order_number', placeholder='If you have an order number, please enter here'),
            Field('name'),
            Field('email'),
            Field('message', placeholder="How can we help?"),
            Reset('reset', 'Reset Form', css_class='btn btn-outline-black rounded-0 text-uppercase mt-5'),
            Submit('submit', 'Submit!', css_class='btn btn-black rounded-0 text-uppercase mt-5'),
        )
        