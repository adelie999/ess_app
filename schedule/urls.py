""" schedule urls """
from django.urls import path
from .views import Schedule
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', Schedule.as_view(), name="index"),
    path('register', views.register, name="register"),
    path('delete', views.delete, name="delete"),
]