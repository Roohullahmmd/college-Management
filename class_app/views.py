from django.shortcuts import render
from .models import Add_class

# Create your views here.

def classes_list(request):
	all_classes = Add_class.objects.all()
	data = {'all_classes': all_classes}
	return render(request, 'classes_list.html', data)

def get_student_class(request, pk):
	get_class = Add_class.objects.get(id=pk)
	all_student = get_class.add_student_set.all()
	data = {'get_class': get_class, 'all_student': all_student}
	return render(request, 'single_class.html', data)

def get_class_subject(request, pk):
	get_class = Add_class.objects.get(id=pk)
	get_subjects = get_class.add_subject_set.all()
	data = {'get_subjects': get_subjects}
	return render(request, 'single_subject.html', data)
