from django import forms

from design.models import Project

class NewProjForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner']

class RateForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'project']