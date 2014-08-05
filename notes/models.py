from django.db import models

class Note(models.Model):
	
	subject = models.TextField()
	content = models.TextField()