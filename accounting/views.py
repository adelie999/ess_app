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
    html_head = """
    <head>
    <meta charset="utf-8"/>
    <meta name="pdfkit-page-size" content="Legal"/>
    <meta name="pdfkit-orientation" content="Landscape"/>
    </head> """
    html_body = list(request.POST.keys())[0]
    html = html_head + html_body
    config = pdfkit.configuration(
        wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(html, 'out.pdf', configuration=config)
    return redirect('accounting:claim')
