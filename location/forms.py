from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Country,State,City

class LocationForm(forms.Form):
    """
    A basic form for Country and State/Province.
    """
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True, label=_('Country'), empty_label=_('Select your country'))
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=True, label=_('State'), empty_label=_('Select your state'))
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True, label=_('City'), empty_label=_('Select your city'))
    