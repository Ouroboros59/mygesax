from django import forms
from django.contrib.auth.models import User

from base.models import Grade, Subject


class GradeCreationForm(forms.ModelForm):
    """
        A form that creates a grade
    """
    error_messages = {
        'message': 'todo.',
    }

    def __init__(self, param=None, *args, **kwargs):
        super(GradeCreationForm, self).__init__(*args, **kwargs)
        self._subject_id = str(param).split("?")[1].split("=")[1][:-2]
        subject = Subject.objects.filter(id=self._subject_id)
        if len(subject) != 0:
            i = 0
            users = list()
            for x in subject.values("users__id"):
                user_id = x["users__id"]
                user_name = subject.values("users__username")[i]["users__username"]
                users.append((user_id, user_name))
                i += 1
            self.fields['user'].choices = users
        else:
            self.fields['user'].choices = []

    class Meta:
        model = Grade
        fields = ("user", "note")

    def save(self, commit=True):
        grade = super().save(commit=False)
        grade.subject = Subject.objects.filter(id=self._subject_id)[0]
        if commit:
            grade.save()
        return grade
