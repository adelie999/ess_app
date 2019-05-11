""" home view """
from django.views.generic import TemplateView


class Home(TemplateView):
    """ Home class """
    template_name = 'home/index.html'