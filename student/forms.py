from django import forms
from .models import Add_student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Add_student
		fields = '__all__'

		labels = {
			'student_name' : 'Enter Student Name',
		}

		widgets = {
            'student_name' :  forms.TextInput(attrs={'placeholder': 'Enter Student Name'}),
            'father_name' :  forms.TextInput(attrs={'placeholder': 'Enter Father Name'}),
		}