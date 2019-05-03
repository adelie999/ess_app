""" this student forms.py """
from django import forms
from tempus_dominus.widgets import TimePicker


class PhotoForm(forms.Form):
    image = forms.ImageField()


class TimeForm(forms.Form):
    """ this TimeForm """
    start_time_field = forms.TimeField(
        label='',
        widget=TimePicker(
            options={
                'format': 'HH:mm',
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
    end_time_field = forms.TimeField(
        label='',
        widget=TimePicker(
            options={
                'format': 'HH:mm',
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
