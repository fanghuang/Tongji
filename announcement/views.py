from django.views.generic import ListView
from TJIPMS.views import LoginRequiredMixin
from announcement.models import Announcement


class AnnouncementListView(LoginRequiredMixin, ListView):
    template_name = ""
    model = Announcement


