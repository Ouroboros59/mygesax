from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

class Promotion(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

class Grade(models.Model):
    note = models.PositiveIntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
