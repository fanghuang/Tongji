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
            title = form.cleaned_data['title']
            leader = form.cleaned_data['leader']
            member1 = form.cleaned_data['member1']
            member2 = form.cleaned_data['member2']
            type = form.cleaned_data['type']
            instructor = form.cleaned_data['instructor']
            description = form.cleaned_data['description']
            print form.cleaned_data

            return HttpResponse(form.cleaned_data)
        else:

            return render(request, self.template_name, {'form': form})