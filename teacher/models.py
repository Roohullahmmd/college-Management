from django.db import models
from class_app.models import Add_class

# Create your models here.

class Skills(models.Model):
	skill_name = models.CharField(max_length=120)

	def __str__(self):
		return self.skill_name

class Add_teacher(models.Model):
	teacher_name = models.CharField(max_length=120)
	qualification = models.CharField(max_length=120, null=True, blank=True)
	select_class = models.ForeignKey(Add_class, on_delete=models.CASCADE)
	religion = models.CharField(max_length=120)
	experience = models.IntegerField()
	select_skills = models.ManyToManyField(Skills)

	def __str__(self):
		return self.teacher_name