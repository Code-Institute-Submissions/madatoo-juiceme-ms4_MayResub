"""form for updating the default address"""
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """form for updating the default address"""
    default_country = forms.CharField(disabled=True, initial='IE')

    class Meta:
        """ all data can be updated except\
        the user and country fields """
        model = UserProfile

        exclude = ('user', 'country',)

    def __init__(self, *args, **kwargs):
        """"add placeholders to the form"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone',
            'default_street_address1': 'Address 1',
            'default_street_address2': 'Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County',
            'default_country': 'IE'
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields['default_country'].required:
                placeholder = f'{placeholders[field]}'
            else:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False