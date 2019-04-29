""" this student view.py """
from django.shortcuts import render
from .models import Students


def home(request):
    """ this home view """
    return render(request, 'student/home.html')


def student_list(request):
    """ this student_list view """
    context = {'all_data': Students.objects.all}
    return render(request, 'student/list.html', context)
