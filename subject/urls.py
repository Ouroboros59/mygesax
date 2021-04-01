from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.get_subject, name='get_subject'),
]