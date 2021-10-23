from django import forms

from design.models import Profile, Project, Rating


class NewProjForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['owner', 'project']

class ProfUpdateForm(forms.ModelForm):
    class Meta:
          model = Profile
          exclude = ['user']          
#          fields = ('pic', 'bio', 'contacts')  