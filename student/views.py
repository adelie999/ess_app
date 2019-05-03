""" this student view.py """
import datetime
import pytz
import shutil
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import Students, Schedules
from .forms import TimeForm


def home(request):
    """ this home view """
    return render(request, 'student/home.html')


def student_register(request):
    """ this student_register view """
    return render(request, 'student/student_register.html')


def form_register(request):
    """ this student_register view """
    print(request.POST)
    # shutil.copy(request.POST.get('cutomfile'), '../static/photo/1.png')
    Students.objects.create(name='test1', birthday='1234', age='6', school_year='1', address='tokyo',
     payment='3000', parent_name='parent', parent_email='testse', parent_phone='090909')
    return redirect('student:student_register')


def student_list(request):
    """ this student_list view """
    context = {'all_data': Students.objects.order_by('school_year')}
    return render(request, 'student/student_list.html', context)


def schedule(request):
    """ this schedule view """
    context = {"form": TimeForm()}
    return render(request, 'student/schedule.html', context)


def ajax_schedule(request):
    """ this ajax action """
    data = serializers.serialize("json", Schedules.objects.all())
    return JsonResponse(data, safe=False)


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
