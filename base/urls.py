from django.urls import path

from .views import get_subject 

urlpatterns = [
    path('new-subject/', get_subject.as_view(), name='new-subject'),
]