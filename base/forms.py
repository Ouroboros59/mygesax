from django import forms
from .models import Promotion, Subject
# from django.contrib.auth.models import User


class ClassForm(forms.ModelForm):
    class Meta:
        model = Promotion

        fields = [
            "name",
            "users"
        ]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject

        fields = [
            "name",
            "description",
            "users"
        ]
