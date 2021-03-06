from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    users = models.ManyToManyField(User)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class Grade(models.Model):
    note = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
