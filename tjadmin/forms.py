from django import forms


class UploadFileForm(forms.Form):
    student_file = forms.FileField()