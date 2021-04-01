from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def index(request):
  context = {}
  context["dataset"] = UserProfile.objects.values('avatar').exclude(avatar="")
  form = UserProfileForm(request.POST or None)
  if form.is_valid():
    form.save()
  context["form"] = form
  return render(request, 'thrombinoscope/index.html', context)
