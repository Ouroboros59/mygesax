from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Grade(models.Model):
    note = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, default="")
