from django.shortcuts import render
from django.views.generic import ListView
from base.models import Promotion

# Create your views here.

class UserPromotionList(ListView):
    model = Promotion
    context_object_name="student_promotions"
    template_name="promotions/index.html"
    def get_queryset(self):
        return Promotion.objects.filter(users=self.request.user)