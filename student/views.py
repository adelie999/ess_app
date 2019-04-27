""" this student view """
from django.http import HttpResponse


def index(request):
    """ index """
    return HttpResponse("Hello, world. You're at the polls index.")
