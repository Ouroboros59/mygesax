from django.db import models
from django.contrib.auth.models import User
from subject.models import Subject

class Promotion(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

class Grade(models.Model):
    note = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)