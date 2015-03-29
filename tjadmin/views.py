import csv
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from account.models import Student
from announcement.models import Announcement
from tjadmin.forms import UploadFileForm


class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffLoginRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class TJAdminLoginView(TemplateView):
    template_name = "tjadmin/login.html"


class AdminView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/tjadmin.html"


class CreateStudentView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/create_student.html"

    def post(self, request):
        student_id = request.POST['student_id']
        name = request.POST['student_name']
        password = request.POST['password']
        start_year = request.POST['start_year']
        student = Student.create_student(student_id, name, password, start_year)
        return HttpResponse(str(student) + " created")


class UploadStudentView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/upload_student.html"

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            student_file = request.FILES['student_file']
            student_list = parse_student_file(student_file)
            return render(request, "tjadmin/upload_student_confirm.html", {'student_list': student_list})
        else:
            return redirect("tjadmin_upload_student")

class UploadStudentConfirmedView(StaffLoginRequiredMixin, TemplateView):

    def get(self, request):
        print request


def parse_student_file(file):
    reader = csv.reader(file)
    stu_list = list(reader)
    return stu_list


class AnnouncementCreate(StaffLoginRequiredMixin, CreateView):

    template_name = "tjadmin/create_announcement.html"
    model = Announcement
