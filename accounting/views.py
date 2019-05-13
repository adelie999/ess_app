""" accounting views """
import pdfkit
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.core import serializers
from .models import Sells


class Sell(TemplateView):
    """ sell class """
    template_name = 'accounting/sell.html'


class Claim(TemplateView):
    """ claim class """
    template_name = 'accounting/claim.html'


class Invoice(TemplateView):
    """ invoice class """
    template_name = 'accounting/invoice.html'


def chart(request):
    """ chart render action """
    data = serializers.serialize("json", Sells.objects.all())
    return JsonResponse(data, safe=False)


def create_pdf(request):
    """ pdf """
    html_text = list(request.POST.keys())
    print(html_text[0])
    pdf_stream = pdfkit.from_string(html_text[0], False)
    print(pdf_stream)
    return redirect('accounting:claim')
