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
    """ スケジュール表示view """

    def get(self, request, *args, **kwargs):
        """ get """
        context = {"form": TimeForm()}
        return render(request, 'schedule/index.html', context)

    def post(self, request, *args, **kwargs):
        """ post """
        data = serializers.serialize("json", Schedules.objects.all())
        return JsonResponse(data, safe=False)

    def register(self, request):
        """ this register action """
        ins_title = request.POST.get('registerTitle')
        start_jst_datetime = request.POST.get(
            'select_day') + ' ' + request.POST.get('start_time_field')
        start_utc_datetime = datetime.datetime.strptime(
            start_jst_datetime, '%Y-%m-%d %H:%M')
        ins_start_day = pytz.utc.localize(start_utc_datetime)
        end_jst_datetime = request.POST.get(
            'select_day') + ' ' + request.POST.get('end_time_field')
        end_utc_datetime = datetime.datetime.strptime(
            end_jst_datetime, '%Y-%m-%d %H:%M')
        ins_end_day = pytz.utc.localize(end_utc_datetime)
        ins_description = request.POST.get('registerDescription')
        Schedules.objects.create(title=ins_title, start_date=ins_start_day, end_date=ins_end_day,
                                description=ins_description)
        return redirect('schedule:index')

    def delete(self, request):
        """ this delete action """
        Schedules.objects.filter(id=request.POST.get('delete_id')).delete()
        return redirect('schedule:index')
