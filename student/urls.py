""" this student urls.py """
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, StudentRegister, StudentShow, ScheduleShow, Account
from . import views

app_name = 'student'
urlpatterns = [
    path('', Home.as_view()),
    path('student/student_register',
         StudentRegister.as_view(), name="student_register"),
    path('student/student_list', StudentShow.as_view()),
    path('student/schedule', ScheduleShow.as_view(), name="schedule"),
    path('student/schedule/register',
         views.schedule_register, name="schedule_register"),
    path('student/schedule/delete',
         views.schedule_delete, name="schedule_delete"),
     path('student/sell', Account.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
