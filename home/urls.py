""" this student urls.py """
from django.urls import path
from .views import Home, Setting

app_name = 'home'
urlpatterns = [
    path('', Home.as_view()),
    path('setting', Setting.as_view()),
]