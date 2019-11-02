from django.db import models

# Create your models here.

class TodoTask(models.Model):
  title = models.CharField(max_length=30)
