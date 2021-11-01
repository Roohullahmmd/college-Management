from django.shortcuts import render, redirect
from teacher.models import Add_teacher
from .models import Add_student
from class_app.models import Add_class
from subject.models import Add_subject
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def student_home(request):
	teacher_count = Add_teacher.objects.all().count()
	student_count = Add_student.objects.all().count()
	class_count = Add_class.objects.all().count()
	subject_count = Add_subject.objects.all().count()
	data = {'teacher_count': teacher_count, 'student_count': student_count, 'class_count': class_count, 
			'subject_count': subject_count}
	return render(request, 'student_home.html', data)

def student_list(request):
	all_students = Add_student.objects.all()

	student_name = ""

	if 'student_name' in request.GET:
		student_name = request.GET['student_name']
		if student_name:
			all_students = all_students.filter(student_name__icontains=student_name)

	if 'father_name' in request.GET:
		father_name = request.GET['father_name']
		if father_name:
			all_students = all_students.filter(father_name__icontains=father_name)

	count = all_students.count()

	data = {'all_students': all_students, 'student_name': student_name, 'count': count}
	return render(request, 'student_list.html', data)

def add_student(request):
	student_form = StudentForm()
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			student_form.save()
			student_name = student_form.cleaned_data.get('student_name')
			messages.success(request, f'Student Added Successfully : ( {student_name} ) ')
			return redirect('student_list')
		else:
			return HttpResponse("Failed...")
	data = {'student_form': student_form}
	return render(request, 'add_student.html', data)


def student_delete(request, pk):
	get_student = Add_student.objects.get(id=pk)
	if request.method == 'POST':
		get_student.delete()
		student_name = get_student.student_name
		messages.error(request, f'Student Deleted : ( {student_name} ) ')
		return redirect('student_list')
	data = {'get_student': get_student}
	return render(request, 'student_delete.html', data)

def student_update(request, pk):
	get_student = Add_student.objects.get(id=pk)
	student_form = StudentForm(instance=get_student)
	if request.method == 'POST':
		student_form = StudentForm(request.POST, instance=get_student)
		if student_form.is_valid():
			student_form.save()
			student_name = get_student.student_name
			messages.warning(request, f'Student Updated : {student_name}')
			return redirect('student_list')
		else:
			return HttpResponse('Updation Failed...')
	data = {'student_form': student_form}
	return render(request, 'student_update.html', data)






