""" this student urls.py """
from django.urls import path
from .views import Home, Setting
from . import views

app_name = 'home'
urlpatterns = [
    path('', Home.as_view()),
    path('setting', Setting.as_view(), name="setting"),
    path('setting/url', views.setting_url, name="setting_url"),
]