from django import forms

from models import *

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
