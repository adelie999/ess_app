""" this student urls.py """
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.home, name='home'),
    path('student/schedule', views.schedule, name='schedule'),
    path('student/student_register',
         views.student_register, name='student_register'),
    path('student/form/register', views.form_register, name='form_register'),
    path('student/student_list', views.student_list, name='student_list'),
    path('student/ajax/schedule', views.ajax_schedule, name="ajax_schedule"),
    path('student/schedule/delete',
         views.schedule_delete, name="schedule_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
