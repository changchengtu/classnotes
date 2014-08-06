from django.db import models

class Note(models.Model):
	subject = models.TextField()
	content = models.TextField()
	authors = models.TextField()
	school = models.TextField()
	department = models.TextField()



