""" student urls """
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Register, List

app_name = 'student'
urlpatterns = [
    path('register', Register.as_view(), name="register"),
    path('list', List.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
