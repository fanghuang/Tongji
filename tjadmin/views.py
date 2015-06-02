import csv
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from announcement.models import Announcement
from tjadmin.forms import UploadFileForm
#from tjadmin.forms import ProjectSearchForm
from project.models import Project
from account.models import Teacher, Student
from django.db import connection, transaction



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
        # return HttpResponse(str(student) + " created")
        return render(request, "tjadmin/upload_successed.html")


class UploadStudentView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/upload_student.html"

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            student_file = request.FILES['student_file']
            student_list = parse_student_file(student_file)
            print student_list
            # return render(request, "tjadmin/upload_student_confirm.html", {'student_list': student_list})
            return render(request, "tjadmin/upload_successed.html")
        else:
            return render(request, "tjadmin/upload_failed.html")


class UploadStudentConfirmedView(StaffLoginRequiredMixin, TemplateView):

    def get(self, request):
        return HttpResponse("success")


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

    def simpleSearch(self, request):
        text = request.POST['simple_search']
#        cursor = connection.cursor()
#        sql = "select * from PROJECT where balbalbalaablabalbal"
        q1 = Project.objects.filter(leader__icontains=text)
        q2 = Project.objects.filter(title__icontains=text)
        q3 = Project.objects.filter(teacher__icontains=text)
        q4 = Project.objects.filter(type__icontains=text)
        projects = q1+q2+q3+q4
        if projects:
            return redirect("tjadmin_upload_student")
        else:
            return render(request, "tjadmin/search_project_list.html", {'project_list': projects})

class ProjectListView(StaffLoginRequiredMixin, TemplateView):
    template_name = "tjadmin/search_project_list.html"


#update user table instead of student table
def parse_student_file(file):
    #Or csv.DictReader
    reader = csv.reader(file)
    #Skip the header
    next(reader)
    for row in reader:
        try:
            student_id = row[0].strip()
            student_name = row[1].strip()
            password = row[2].strip()
            start_year = row[3].strip()
            Student.create_student(student_id, student_name, password, start_year)
        except Exception as e:
            print e

    return ["DONE!"]


class AnnouncementCreate(StaffLoginRequiredMixin, CreateView):
    model = Announcement
    template_name = "tjadmin/create_announcement.html"

