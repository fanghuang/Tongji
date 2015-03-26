from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required

class StaffLoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(staff_member_required, cls).as_view(**initkwargs)
        return staff_member_required(view)


class LoginView(TemplateView):
    template_name = "tjadmin/login.html"

class AdminView(TemplateView):
    template_name = "tjadmin/tjadmin.html"



class CreateStudentView(TemplateView,StaffLoginRequiredMixin):

    template_name = "tjadmin/create_student.html"

    def post(self, request):
        pass
        # TODO
        # handle post
        # create custom user model