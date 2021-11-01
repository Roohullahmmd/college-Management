from django.shortcuts import render, redirect
from subject.models import Add_subject
from .forms import SubjectForm

def subject_list(request):
	all_subjects = Add_subject.objects.all()
	data={'all_subjects':all_subjects}
	return render(request,'subject_list.html', data)


def add_subject(request):
	subject_form=SubjectForm()
	if request.method=='POST':
		subject_form=SubjectForm(request.POST)
		if subject_form.is_valid():
			subject_form.save()
			return redirect('subject_list')
	data={'subject_form':subject_form}
	return render(request, 'add_subject.html', data)


def update_subject(request, pk):
	get_subject=Add_subject.objects.get(id=pk)
	subject_form=SubjectForm(instance=get_subject)
	if request.method=='POST':
		get_subject=SubjectForm(request.POST, instance=get_subject)
		if subject_form.is_valid():
			subject_form.save()
			return redirect('subject_list')
	data={'subject_form':subject_form}
	return render(request,'update_subject.html', data)


def delete_subject(request, pk):
	get_subject=Add_subject.objects.get(id=pk)
	if request.method=='POST':
		get_subject.delete()
		return redirect('subject_list')
	data={'get_subject':get_subject}
	return render(request, 'delete_subject.html', data)