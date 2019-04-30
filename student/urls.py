""" this student urls.py """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/schedule', views.schedule, name='schedule'),
    path('student/list', views.student_list, name='student_list'),
    path('student/ajax/schedule', views.ajax_schedule, name="ajax_schedule")
]
