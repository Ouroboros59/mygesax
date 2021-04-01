from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('export/', views.csv_export, name='csv_export'),
    path('import/', views.csv_import, name='csv_import'),
    path('import-doc/', views.import_doc, name='import_doc'),
]