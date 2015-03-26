from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "account/login.html"


