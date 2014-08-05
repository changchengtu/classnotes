from django.db import models

class Note(models.Model):
	date = models.DateTimeField()
	subject = models.TextField()
	context = models.TextField()