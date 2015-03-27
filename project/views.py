from django.shortcuts import render
from django.views.generic import TemplateView
from TJIPMS.views import LoginRequiredMixin


class ProposalCreateView(LoginRequiredMixin, TemplateView):
    template_name = "project/create_proposal.html"