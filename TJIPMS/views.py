from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"