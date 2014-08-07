from django.db import models

class Note(models.Model):
	subject = models.TextField()
	content = models.TextField()
	authors = models.TextField()
	tag = models.TextField(null=True)
	school_name = models.TextField()
	department_name = models.TextField()
	class_name = models.TextField()




