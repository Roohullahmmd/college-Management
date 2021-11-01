from django import forms
from .models import Add_teacher


class TeacherForm(forms.ModelForm):
	class Meta:
		model=Add_teacher
		fields='__all__'