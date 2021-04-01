from django.urls import path

from .views import AddGradeView, UserGradeView

urlpatterns = [
    path('add/grades/', AddGradeView.as_view(), name='add grade'),
    path('', UserGradeView.as_view(), name='get_grade'),
]
