from django.db import models
from class_app.models import Add_class

# Create your models here.

class Student_fee(models.Model):
	select_class = models.ForeignKey(Add_class, on_delete=models.CASCADE)
	fee = models.IntegerField()

class Add_student(models.Model):
	student_name = models.CharField(max_length=120)
	father_name = models.CharField(max_length=120)
	address = models.CharField(max_length=120, null=True, blank=True)
	select_class = models.ForeignKey(Add_class, on_delete=models.CASCADE)
	religion = models.CharField(max_length=1200)

	def __str__(self):
		return self.student_name
