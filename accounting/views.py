""" accounting views """
from django.views.generic import TemplateView


class Sell(TemplateView):
    """ sell class """
    template_name = 'accounting/sell.html'


class Claim(TemplateView):
    """ claim class """
    template_name = 'accounting/claim.html'
