from django.db import models
from django.contrib.auth.models import User, AbstractUser


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.TextField(default="")

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    users = models.ManyToManyField(User)
    
class Promotion(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User)
    subjects = models.ManyToManyField(Subject)


class Grade(models.Model):
    note = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
