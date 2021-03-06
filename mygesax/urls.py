from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject/', include('subject.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('supervisor/', include('base.urls')),
    path('', HomeView.as_view(), name='home'),

    path('promotions/', views.UserPromotionList.as_view(), name="promotions"),
    path('promotions/<name>', views.PromoList.as_view(), name="promotion"),
    path('class/', views.TeacherClassList.as_view(), name="class"),
]
