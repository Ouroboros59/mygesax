from django.urls import reverse_lazy
from django.views import generic

from subject.form import GradeCreationForm


class AddGrade(generic.CreateView):
    form_class = GradeCreationForm
    success_url = reverse_lazy('/')
    template_name = 'grades/add.html'
