from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ClassForm, SubjectForm, MyUserChangeForm
from .models import Promotion, Subject


@login_required
@permission_required('base.delete_promotion')
def index(request):
    return render(request, 'supervisor/index.html')


@login_required
@permission_required('auth.delete_user')
def manage_user(request):
  print(request.user.id)
  context = {}
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    form.save()
  context["form"] = form
  context["dataset"] = User.objects.exclude(is_staff = True).exclude(id = request.user.id)
  return render(request, 'supervisor/manage-user.html', context)


@login_required
@permission_required('base.delete_promotion')
def manage_class(request):
    context = {}
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    context["dataset"] = Promotion.objects.all()
    return render(request, 'supervisor/manage-class.html', context)

@login_required
@permission_required('base.delete_subject')
def manage_subject(request):
    context = {}
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    context["dataset"] = Subject.objects.all()
    return render(request, 'supervisor/manage-subject.html', context)

@login_required
@permission_required('auth.delete_user')
def detail_user(request, id):
  context = {}
  obj = get_object_or_404(User, id = id)
  form = MyUserChangeForm(request.POST or None, instance = obj)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/supervisor/user")
  context["form"] = form
  return render(request, 'supervisor/detail-user.html', context)

@login_required
@permission_required('base.delete_promotion')
def detail_class(request, id):
  context = {}
  obj = get_object_or_404(Promotion, id = id)
  form = ClassForm(request.POST or None, instance = obj)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/supervisor/class")
  context["form"] = form
  return render(request, 'supervisor/detail-class.html', context)

@login_required
@permission_required('base.delete_subject')
def detail_subject(request, id):
  context = {}
  obj = get_object_or_404(Subject, id = id)
  form = SubjectForm(request.POST or None, instance = obj)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/supervisor/subject")
  context["form"] = form
  return render(request, 'supervisor/detail-subject.html', context)

@login_required
@permission_required('auth.delete_user')
def delete_user(request, id):
  obj = get_object_or_404(User, id = id)
  obj.delete()
  return JsonResponse({"id": id})

@login_required
@permission_required('base.delete_subject')
def delete_subject(request, id):
  obj = get_object_or_404(Subject, id = id)
  obj.delete()
  return JsonResponse({"id": id})

@login_required
@permission_required('base.delete_promotion')
def delete_class(request, id):
  obj = get_object_or_404(Promotion, id = id)
  obj.delete()
  return JsonResponse({"id": id})
