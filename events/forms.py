from django import forms
from .models import Resistration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Resistration
        fields = ('name','event', 'email', 'phone_number', 'address',
            'how_did_you_hear_about_this_event')
