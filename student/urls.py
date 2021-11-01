from django.urls import path
from . import views

urlpatterns = [
	path('', views.student_home, name='student_home'),
	path('student_list/', views.student_list, name='student_list'),
	path('add_student/', views.add_student, name='add_student'),
	path('student_delete/<str:pk>/', views.student_delete, name='student_delete'),
	path('student_update/<str:pk>/', views.student_update, name='student_update'),
]
