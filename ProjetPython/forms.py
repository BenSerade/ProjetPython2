from django import forms
from .models import Session, FormSubmission

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['form_status', 'opening_time', 'closing_time']

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = ['progress_percentage', 'difficulty_level', 'personal_progress']
