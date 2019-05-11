""" schedule urls """
from django.urls import path
from .views import Schedule
from . import views

app_name = 'schedule'
urlpatterns = [
    path('index', Schedule.as_view(), name="index"),
    path('register', Schedule.register, name="register"),
    path('delete', Schedule.delete, name="delete"),
]