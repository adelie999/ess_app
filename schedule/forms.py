""" schedule forms """
from django import forms
from tempus_dominus.widgets import TimePicker


class TimeForm(forms.Form):
    """ TimeForm class """
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
