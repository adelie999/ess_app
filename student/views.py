""" this student view.py """
import datetime
import pytz
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.core import serializers
from .models import Students, Schedules
from .forms import TimeForm, StudentsForm


class Home(TemplateView):
    """ ホームview """
    template_name = 'student/home.html'


class StudentRegister(CreateView):  # pylint: disable=too-many-ancestors
    """ 生徒登録view """
    model = Students
    fields = ["name", "birthday", "age", "school_year", "address",
              "photo_path", "payment", "parent_name", "parent_email", "parent_phone"]

    def get(self, request, *args, **kwargs):
        context = {"form": StudentsForm()}
        return render(request, 'student/student_register.html', context)

    def post(self, request, *args, **kwargs):
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            insert_query = Students()
            # insert_query.name = form.changed_data[0]
            # insert_query.birthday = form.changed_data[1]
            # insert_query.age = form.changed_data[2]
            # insert_query.school_year = form.cleaned_data[3]
            # 後で追加する
            insert_query.photo_path = form.cleaned_data['image']
            insert_query.save()
        else:
            pass
        return redirect('student:student_register')


class StudentShow(ListView):  # pylint: disable=too-many-ancestors
    """ 生徒表示view """
    model = Students
    template_name = 'student/student_list.html'

    def get_queryset(self):
        return Students.objects.order_by('school_year')


class ScheduleShow(TemplateView):
    """ スケジュール表示view """

    def get(self, request, *args, **kwargs):
        """ get """
        context = {"form": TimeForm()}
        return render(request, 'student/schedule.html', context)

    def post(self, request, *args, **kwargs):
        """ post """
        data = serializers.serialize("json", Schedules.objects.all())
        return JsonResponse(data, safe=False)

class Account(TemplateView):
    template_name = 'student/sell.html'


def schedule_register(request):
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
    return redirect('student:schedule')


def schedule_delete(request):
    """ this delete action """
    Schedules.objects.filter(id=request.POST.get('delete_id')).delete()
    return redirect('student:schedule')
