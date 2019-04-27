""" this admin.py """
from django.contrib import admin
from .models import Students, Parents

admin.site.register(Students)
admin.site.register(Parents)
