from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

from django.utils.translation import ugettext as _


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(LoginRequiredMixin, View):
    template_name = "index.html"

    def get(self, request):
        user = request.user

        leading_project = None
        involved_project = None
        try:
            leading_project = user.student.leading_project.all()
            involved_project = user.student.involved_project.all()
        except:
            pass

        return render(request, self.template_name,
                      {"leading_project": leading_project, "involved_project": involved_project})
