""" student views """
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Students
from .forms import StudentsForm


class Register(CreateView):  # pylint: disable=too-many-ancestors
    """ Register class """
    model = Students
    fields = ["name", "birthday", "age", "school_year", "address",
              "photo_path", "payment", "parent_name", "parent_email", "parent_phone"]

    def get(self, request, *args, **kwargs):
        context = {"form": StudentsForm()}
        return render(request, 'student/register.html', context)

    def post(self, request, *args, **kwargs):
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            insert_query = Students()
            # insert_query.name = form.changed_data[0]
            # insert_query.birthday = form.changed_data[1]
            # insert_query.age = form.changed_data[2]
            # insert_query.school_year = form.cleaned_data[3]
            # 後で追加する
            insert_query.photo_path = form.cleaned_data['image']
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
