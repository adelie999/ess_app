""" this student urls.py """
from django.urls import path
from .views import Sell, Claim

app_name = 'accounting'
urlpatterns = [
    path('sell', Sell.as_view()),
    path('claim', Claim.as_view()),
]
