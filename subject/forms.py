from django.shortcuts import render
from django import forms
from .models import Subject

# Create your views here.
class SubjectForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=30)
    description = forms.CharField(label="Description", max_length=50)

    class Meta():
        model = Subject
        fields = ['name', 'description']