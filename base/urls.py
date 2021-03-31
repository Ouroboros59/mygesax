from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', views.manage_user, name="user"),
    path('class/', views.manage_class, name="class"),
    path('subject/', views.manage_subject, name="subject")
]
