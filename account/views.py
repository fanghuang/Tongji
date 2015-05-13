from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import translation
from django.views.generic import TemplateView, View, UpdateView
from TJIPMS.views import LoginRequiredMixin
from tjadmin.views import StaffLoginRequiredMixin
from account.models import Student


class LoginView(TemplateView):
    template_name = "account/login.html"
    #TODO why user is none? 
    def post(self, request):
        student_id = request.POST['student_id']
        password = request.POST['password']
        print student_id, password
        language = request.POST['language']
        remember_me = request.POST.getlist('remember_me')
        user = authenticate(student_id=student_id, password=password)
        print user
        if language == 'en' or language == 'zh-cn':
            user_language = language
            translation.activate(user_language)
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        if user is not None:
            if user.is_active:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(600)
                if user.is_staff:
                    return redirect("tjadmin")
                else:
                    return redirect("index")
            else:
                return HttpResponse("disabled account")
        else:
            return render(request, "account/login.html", {'invalid': True})

#individual profile and setting share same templates -- individual.html
class ProfileView(LoginRequiredMixin, UpdateView):

    model = Student
    fields = ['phone', 'email']
    template_name = "account/individual.html"

    def get_object(self):
        return self.request.user.student


class SettingView(LoginRequiredMixin, View):

    template_name = "account/individual.html"

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
        else:
            return render(request, self.template_name, {'form': form})

class SuperuserView(StaffLoginRequiredMixin, TemplateView):

    template_name = "tjadmin/tjadmin.html"
