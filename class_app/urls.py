from django.urls import path
from . import views

urlpatterns = [
	path('classes_list/', views.classes_list, name='classes_list'),
	path('get_student_class/<str:pk>', views.get_student_class, name='get_student_class'),
	path('get_class_subject/<str:pk>/', views.get_class_subject, name='get_class_subject')
]
