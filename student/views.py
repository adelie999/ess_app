""" this student view.py """
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import Students, Schedule
from .forms import TimeForm


def home(request):
    """ this home view """
    return render(request, 'student/home.html')


def student_list(request):
    """ this student_list view """
    context = {'all_data': Students.objects.order_by('student_school_year')}
    return render(request, 'student/list.html', context)


def schedule(request):
    """ this schedule view """
    context = {"form": TimeForm(), "form2": TimeForm()}
    return render(request, 'student/schedule.html', context)


def ajax_schedule(request):
    """ this ajax action """
    data = serializers.serialize("json", Schedule.objects.all())
    return JsonResponse(data, safe=False)


def schedule_delete(request):
    """ this ajax action """
    Schedule.objects.filter(id=request.POST.get('delete_id')).delete()
    return redirect('student:schedule')
