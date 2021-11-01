from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_page, name='main_page'),
	path('login_page/', views.login_page, name='login_page'),
	path('login_check/', views.login_check, name='login_check'),
	path('logout_user/', views.logout_user, name='logout_user')
]
