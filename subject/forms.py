from django import forms
from .models import Add_subject

class SubjectForm(forms.ModelForm):
	class Meta:
		model=Add_subject
		fields='__all__'