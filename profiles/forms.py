from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form for the user updating the details in the profile
    """
    class Meta:
        model = UserProfile
        # rendering all fields except for the user
        # the username cannot be changed
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes for the default information
        for the user's shipping information
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # Add classes to the form to match the theme of the site
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False