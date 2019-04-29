""" this student urls.py """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/list', views.student_list, name='student_list'),
]
