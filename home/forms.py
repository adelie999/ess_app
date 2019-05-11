""" schedule forms """
from django import forms
from .models import Settings


class SettingsForm(forms.ModelForm):
    """ SettingsForm class """

    class Meta:
        model = Settings
        fields = ('name', 'url')
