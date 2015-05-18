from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import translation
from django.views.generic import View

from django.utils.translation import ugettext as _

from django.http import HttpResponse
from django.http.request import (HttpRequest, QueryDict,
    RawPostDataException, UnreadablePostError, build_request_repr)

from project.models import Project

import json

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
                      {"leading_project": leading_project,
                      "involved_project": involved_project,
                      "type_option":Project.TYPE_CHOICES})


def language_switch(request):
    language = request.GET['code']
    next = request.GET['next']
    user_language = language
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect(next)

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
        # post.status = status
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

        post.delete()

        response_data = {}
        response_data['msg'] = 'Project was deleted.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )