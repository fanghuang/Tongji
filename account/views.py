from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "account/login.html"

    def post(self, request):
        student_id = request.POST['student_id']
        password = request.POST['password']

        user = authenticate(student_id=student_id,password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("success")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid login")
