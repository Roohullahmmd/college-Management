from django.db import models
from class_app.models import Add_class

# Create your models here.


class Add_subject(models.Model):
	subject_name = models.CharField(max_length=120)
	select_class = models.ForeignKey(Add_class, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject_name