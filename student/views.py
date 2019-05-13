""" student views """
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Students
from .forms import StudentsForm


class Register(CreateView):  # pylint: disable=too-many-ancestors
    """ Register class """
    model = Students

    def get(self, request, *args, **kwargs):
        context = {"form": StudentsForm()}
        return render(request, 'student/register.html', context)

    def post(self, request, *args, **kwargs):
        form = StudentsForm(request.FILES, request.FILES)
        print(request.POST)
        if form.is_valid():
            insert_query = Students()
            insert_query.name = request.POST.get('studentName')
            insert_query.birthday = request.POST.get('studentBirthday')
            insert_query.age = request.POST.get('studentAge')
            insert_query.school_year = request.POST.get('schoolYear')
            insert_query.address = request.POST.get('studentAddress')
            insert_query.photo_path = form.cleaned_data['image']
            insert_query.remarks = request.POST.get('remarks')
            insert_query.parent_name = request.POST.get('parentName')
            insert_query.parent_email = request.POST.get('parentEmail')
            insert_query.parent_phone = request.POST.get('parentPhone')
            insert_query.payment = request.POST.get('payment')
            print("success")
            insert_query.save()
        else:
            pass
        return redirect('student:register')


class List(ListView):  # pylint: disable=too-many-ancestors
    """ List class """
    model = Students
    template_name = 'student/list.html'

    def get_queryset(self):
        return Students.objects.order_by('school_year')
