""" this student urls.py """
from django.urls import path
from .views import Sell, Claim
from . import views

app_name = 'accounting'
urlpatterns = [
    path('sell', Sell.as_view()),
    path('sell/chart', views.chart),
    path('claim', Claim.as_view()),
]
