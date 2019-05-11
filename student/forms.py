""" this student forms.py """
from django import forms


class StudentsForm(forms.Form):
    """ register """
    image = forms.ImageField()
