from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubjectForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_subject(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubjectForm()

    return render(request, 'subject/new.html', {'form': form})
