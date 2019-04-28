""" this student view.py """
from django.shortcuts import render

def home(request):
    """ this home view """
    return render(request, 'student/home.html')
