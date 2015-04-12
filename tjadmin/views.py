import csv
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from account.models import Student
from announcement.models import Announcement
from tjadmin.forms import UploadFileForm
# from tjadmin.form import ProjectSearchForm
from project.models import Project
from account.models import Teacher


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
        #TODO
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


class ProjectSearchView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/search_project.html"

    def post(self, request):
        title = request.POST['title']
        leader = request.POST['leader']
        teacher_name = request.POST['teacher']
        type = request.POST['type']
        # approved = request.POST['approved_time']
        # finished = request.POST['finished_time']
        teachers = Teacher.objects.filter(name=teacher_name)
        teacher = teachers[0]
        projects = Project.objects.filter(leader=leader, title=title, teacher=teacher, type=type)
                                         # approved_time=approved, finished_time=finished)
        for project in projects:
            print project.title

        return render(request, "tjadmin/search_project_list.html", {'project_list': projects})


class ProjectListView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/search_project_list.html"



def parse_student_file(file):
    reader = csv.reader(file)
    stu_list = list(reader)
    return stu_list


class AnnouncementCreate(StaffLoginRequiredMixin, CreateView):
    model = Announcement
    template_name = "tjadmin/create_announcement.html"

