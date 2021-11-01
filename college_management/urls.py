from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_account.urls')),
    path('', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('subject/', include('subject.urls')),
    path('class_app/', include('class_app.urls'))
]
