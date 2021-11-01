from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.

def main_page(request):
	return render(request, 'main_page.html')

def login_page(request):
	return render(request, 'login.html')

def login_check(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('student_home')
		else:
			return redirect('login_page')

def logout_user(request):
	auth.logout(request)
	return redirect('main_page')

