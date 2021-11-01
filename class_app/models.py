from django.db import models

# Create your models here.

class Add_class(models.Model):
	class_name = models.CharField(max_length=120)

	def __str__(self):
		return self.class_name