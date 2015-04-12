from django import forms
from project.models import Project
from django.utils.translation import ugettext_lazy as _

class UploadFileForm(forms.Form):
    student_file = forms.FileField()


# class ProjectSearchForm(forms.Form):
#     title = forms.CharField(label=_("Title"), max_length=50,
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     leader = forms.IntegerField(label=_("Leader"),
#                                 widget=forms.TextInput(
#                                     attrs={'class': 'form-control', 'placeholder': _('Student ID'), 'readonly':True}))
#     type = forms.ChoiceField(label=_("Type"), choices=Project.TYPE_CHOICES,
#                              widget=forms.Select(attrs={'class': 'form-control'}, choices=Project.TYPE_CHOICES))
#     instructor = forms.CharField(label=_("Instructor"), max_length=5,
#                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
#     approved = forms.DataTimeField(label=_("Approved Time"),
#                                    widget=forms.DataTimeField(attrs={'class': 'form-control'}))
#     finished = forms.DataTimeField(label=_("Finished Time"),
#                                    widget=forms.DataTimeField(attrs={'class': 'form-control'}))
