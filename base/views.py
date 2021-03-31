from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ClassForm, SubjectForm
from .models import Promotion, Subject


@login_required
@permission_required('base.add_grade')
def index(request):
    return render(request, 'teacher/index.html')


# @login_required
# @permission_required('base.add_user')
def manage_user(request):
    return render(request, 'teacher/manage-user.html')


# @login_required
# @permission_required('base.add_')
def manage_class(request):
    context = {}
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    context["dataset"] = Promotion.objects.all()
    return render(request, 'teacher/manage-class.html', context)


# @login_required
# @permission_required('base.add_grade')
def manage_subject(request):
    context = {}
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    context["dataset"] = Subject.objects.all()
    return render(request, 'teacher/manage-subject.html', context)
