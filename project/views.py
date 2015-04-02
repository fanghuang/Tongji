from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from TJIPMS.views import LoginRequiredMixin
from account.models import Teacher, Student
from project.forms import ProposalForm
from project.models import Project


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
