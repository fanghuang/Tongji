from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, UpdateView
from TJIPMS.views import LoginRequiredMixin
from account.models import Teacher, Student
from project.forms import ProposalForm
from project.models import Project
from django.http import HttpResponse
from django.http.request import (HttpRequest, QueryDict,
                                 RawPostDataException, UnreadablePostError, build_request_repr)
from django.contrib.admin.views.decorators import staff_member_required
from itertools import chain
import json


class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffLoginRequiredMixin, cls).as_view(**initkwargs)
        return staff_member_required(view)


class ProposalCreateView(LoginRequiredMixin, View):
    template_name = "project/create_proposal.html"


    def get(self, request):
        form = ProposalForm(initial={'leader': request.user.username})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProposalForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            member1 = form.cleaned_data['member1']
            member2 = form.cleaned_data['member2']
            type = form.cleaned_data['type']
            instructor_name = form.cleaned_data['instructor']
            description = form.cleaned_data['description']
            instructor, created = Teacher.objects.get_or_create(name=instructor_name)
            project = Project(title=title, leader=request.user.student, type=type, description=description,
                              teacher=instructor)
            project.save()

            if member1:
                try:
                    member1 = Student.objects.get(student_id=member1)

                except ObjectDoesNotExist:
                    pass
                project.members.add(member1)
            if member2:
                try:
                    member2 = Student.objects.get(student_id=member2)

                except ObjectDoesNotExist:
                    pass
                project.members.add(member2)

            return redirect('index')
        else:

            return render(request, self.template_name, {'form': form})


class ProjectDetailView(DetailView):
    model = Project

    def get_object(self, *args, **kwargs):
        project = super(ProjectDetailView, self).get_object(*args, **kwargs)
        student = self.request.user.student
        if project.leader != student and student not in project.members.all():
            raise PermissionDenied()
        else:
            return project


class ProjectSearchingView(StaffLoginRequiredMixin, DetailView):
    template_name = "project/search_list.html"

    def get(self, request):
        master_project = Project.objects.all()
        return render(request, self.template_name,
                      {"master_project": master_project})


def update_post(request):
    if request.method == 'POST':
        leader = request.POST.get('postleader')
        teacher = request.POST.get('postteacher')
        type = request.POST.get('posttype')
        description = request.POST.get('postdes')
        status = request.POST.get('poststatus')
        print status, description, type
        response_data = {}
        post = Project.objects.get(id=int(QueryDict(request.body).get('postpk')))
        # post.leader = leader
        # post.teacher = teacher
        post.type = type
        post.status = status
        post.description = description
        post.save()
        # Project.objects.filter(id=int(QueryDict(request.body).get('postpk'))).update(description=description)

        response_data['result'] = 'Create post successful!'
        response_data['text'] = post.description
        response_data['status'] = post.status

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def delete_post(request):
    if request.method == 'DELETE':

        post = Project.objects.get(id=int(QueryDict(request.body).get('postpk')))
        print post
        if request.user.is_staff or request.user == post.leader:
            print request.user
            post.delete()
            response_data = {'msg': 'Project was deleted.'}
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse('Not Authorized')
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def search_title(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        if not search_text:
            search_text = "Nothing to Search"

    r1 = Project.objects.filter(title__contains=search_text)
    r2 = Project.objects.filter(status__contains=search_text)
    project = sorted(chain(r1, r2))
    # project = Project.objects.filter(status__contains=search_text) or Project.objects.filter(title__contains=search_text)

    return render(request, "project/search_result.html", 
        {"project": project,
        "type_option":Project.TYPE_CHOICES,
        "status_option":Project.STATUS_CHOICES})


class ProjectListView(StaffLoginRequiredMixin, DetailView):
    template_name = "project/project_list.html"

    def get(self, request):
        master_project = Project.objects.all()
        return render(request, self.template_name,
                      {"master_project": master_project, 
                      "type_option":Project.TYPE_CHOICES,
                      "status_option":Project.STATUS_CHOICES})

def filter_type(request):
    if request.method == "POST":
        filter_type = request.POST['filter_type']
        if filter_type!='ALL' and filter_type!=None:
            master_project = Project.objects.filter(type=filter_type)
        else:
            master_project = Project.objects.all().order_by('status')

    return render(request, "project/project_list_detail.html", 
        {"master_project": master_project,
        "type_option":Project.TYPE_CHOICES,
        "status_option":Project.STATUS_CHOICES})

class ProjectUpdate(DetailView):
    model = Project
    model1 = Student

    fields = ['title', 'leader', 'description', 'type']
    template_name = "project/project_update.html"

    def get_object(self):
        print "================"
        print self.request.user.first_name
        print "================"
        print self.request.user.id
        print "================"
        project = super(ProjectUpdate, self).get_object()
        print project
        print "================"
        return self.request.user.student

