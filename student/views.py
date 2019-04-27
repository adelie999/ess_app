""" this student view.py """
from django.shortcuts import render

def index(request):
    """ index """
    return render(request, 'student/index.html')
