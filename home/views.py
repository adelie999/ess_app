""" home view """
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.core import serializers
from .models import Settings


class Home(TemplateView):
    """ Home class """
    template_name = 'home/index.html'


class Setting(ListView):  # pylint: disable=too-many-ancestors
    """ Setting class """
    model = Settings
    template_name = "home/setting.html"

    def post(self, request, *args, **kwargs):
        """ post method """
        form = request.POST
        for i in range(1, len(form)):
            Settings.objects.filter(pk=i).update(url=form[f'{i}'])
        return redirect('home:setting')


def setting_url(request):
    """ base setting link url  """
    data = serializers.serialize("json", Settings.objects.all())
    return JsonResponse(data, safe=False)
