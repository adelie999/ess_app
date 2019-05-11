""" schedule views """
import datetime
import pytz
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core import serializers
from .models import Schedules
from .forms import TimeForm


class Schedule(TemplateView):
    """ Schedule class """

    def get(self, request, *args, **kwargs):
        """ get """
        context = {"form": TimeForm()}
        return render(request, 'schedule/index.html', context)

    def post(self, request, *args, **kwargs):
        """ post """
        data = serializers.serialize("json", Schedules.objects.all())
        return JsonResponse(data, safe=False)


def register(request):
    """ register action """
    ins_title = request.POST.get('register_title')
    select_day = request.POST.get('select_day')
    ins_start_day = change_jst(select_day + ' ' + request.POST.get('start_time_field'))
    ins_end_day = change_jst(select_day + ' ' + request.POST.get('end_time_field'))
    ins_description = request.POST.get('registerDescription')
    Schedules.objects.create(title=ins_title, start_date=ins_start_day, end_date=ins_end_day,
                             description=ins_description)
    return redirect('schedule:index')


def delete(request):
    """ delete action """
    Schedules.objects.filter(id=request.POST.get('delete_id')).delete()
    return redirect('schedule:index')


def change_jst(utc):
    """ utc -> jst """
    format_date = datetime.datetime.strptime(utc, '%Y-%m-%d %H:%M')
    return pytz.utc.localize(format_date)
