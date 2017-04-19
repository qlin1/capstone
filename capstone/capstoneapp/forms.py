from django import forms
from django.contrib.auth.models import User

from models import *
class PatientForm(forms.Form):
    patientId = forms.CharField(label='patientId', max_length=20)

    def clean_patientId(self):
        patientId = self.cleaned_data['patientId']
        return patientId

class CommentForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['comments'];

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        content = cleaned_data.get('comments')
        if len(content) > 420:
            raise forms.ValidationError("the comment should be less 420 characters")

        return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password',)
        fields = ('first_name', 'last_name','password')