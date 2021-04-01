from django import forms
from .models import Promotion, Subject
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ClassForm(forms.ModelForm):
    class Meta:
        model = Promotion

        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject

        fields = '__all__'

class MyUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['groups', 'first_name', 'last_name', 'email', 'username']