from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from TJIPMS.views import LoginRequiredMixin
from project.forms import ProposalForm


class ProposalCreateView(LoginRequiredMixin, View):

    template_name = "project/create_proposal.html"


    def get(self, request):
        form = ProposalForm(initial={'leader': request.user.username})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProposalForm(request.POST)
        if form.is_valid():
            return HttpResponse('/thanks/')
        else:
            print form.errors
            
            return render(request, self.template_name, {'form': form})