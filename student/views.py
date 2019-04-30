""" this student view.py """
from django.http.response import JsonResponse
from django.shortcuts import render
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
    ret = {"title": "戻り値:", "start":"2019-04-01", "end":"2019-04-01"}
    return JsonResponse(ret)
