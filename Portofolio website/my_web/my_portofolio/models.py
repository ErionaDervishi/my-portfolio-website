# models.py
from django.db import models

class AboutMe(models.Model):
    content = models.TextField()

class Contact_model(models.Model):
    email = models.EmailField()
 


class Project_model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='projects/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title