""" student forms """
from django import forms


class StudentsForm(forms.Form):
    """ StudentsForm class """
    image = forms.ImageField()
