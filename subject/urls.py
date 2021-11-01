from django.urls import path
from . import views
urlpatterns = [
	path('subject_list/', views.subject_list, name='subject_list'),
	path('add_subject/', views.add_subject, name='add_subject'),
	path('update_subject/<str:pk>/', views.update_subject, name='update_subject'),
	path('delete_subject/<str:pk>/', views.delete_subject, name='delete_subject')

]