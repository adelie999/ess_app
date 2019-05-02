""" this student view.py """
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import Students, Schedule


def home(request):
    """ this home view """
    return render(request, 'student/home.html')


def student_list(request):
    """ this student_list view """
    context = {'all_data': Students.objects.order_by('student_school_year')}
    return render(request, 'student/list.html', context)


def schedule(request):
    """ this schedule view """
    return render(request, 'student/schedule.html')


def ajax_schedule(request):
    """ this ajax action """
    temp = serializers.serialize("json", Schedule.objects.all())
    return JsonResponse(temp, safe=False)


def ajax_schedule_delete(request):
    """ this ajax action """
    print(request.POST.get('delete_id'))
    return redirect('student:schedule')
