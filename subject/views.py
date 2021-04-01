from django.urls import reverse_lazy
from django.views import generic

from subject.form import GradeCreationForm


class AddGradeView(generic.FormView):
    form_class = GradeCreationForm
    success_url = reverse_lazy('home')
    template_name = 'grades/add.html'

    def get_form_kwargs(self):
        kwargs = super(AddGradeView, self).get_form_kwargs()
        kwargs['param'] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AddGradeView, self).form_valid(form)
