from django.urls import path

from .views import AddGradeView

urlpatterns = [
    path('add/grades/', AddGradeView.as_view(), name='add grade'),
]
