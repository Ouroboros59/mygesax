from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('base.add_grade')
def index(request):
  return render(request, 'base/index.html')
