from django import forms
from project.models import Project
from django.utils.translation import ugettext_lazy as _


class ProposalForm(forms.Form):
    title = forms.CharField(label=_("Proposal Title"), max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    leader = forms.IntegerField(label=_("Leader"),
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': _('Student ID'), 'readonly':""}))
    member1 = forms.IntegerField(label=_("Member"), required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': _('Student ID')}))
    member2 = forms.IntegerField(label=_("Member"), required=False,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': _('Student ID')}))
    type = forms.ChoiceField(label=_("Type"), choices=Project.TYPE_CHOICES,
                             widget=forms.Select(attrs={'class': 'form-control'}, choices=Project.TYPE_CHOICES))
    instructor = forms.CharField(label=_("Instructor"), max_length=5,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label=_("Description"),
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))