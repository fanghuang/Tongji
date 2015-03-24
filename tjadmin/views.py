from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from account.models import Student


class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffLoginRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class TJAdminLoginView(TemplateView):
    template_name = "tjadmin/login.html"

class AdminView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/tjadmin.html"



class CreateStudentView(TemplateView, StaffLoginRequiredMixin):

    template_name = "tjadmin/create_student.html"

    def post(self, request):
        student_id = request.POST['student_id']
        name = request.POST['student_name']
        password = request.POST['password']
        start_year = request.POST['start_year']
        student = Student.create_student(student_id, name, password, start_year)
        return HttpResponse(str(student)+" created")
