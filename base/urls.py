from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', views.manage_user, name="user"),
    path('class/', views.manage_class, name="class"),
    path('subject/', views.manage_subject, name="subject"),
    path('user/detail/<id>/', views.detail_user, name="user-detail"),
    path('class/detail/<id>/', views.detail_class, name="class-detail"),
    path('subject/detail/<id>/', views.detail_subject, name="subject-detail"),
    path('user/<id>/', views.delete_user, name="user-delete"),
    path('subject/<id>/', views.delete_subject, name="subject-delete"),
    path('class/<id>/', views.delete_class, name="class-delete")
]
