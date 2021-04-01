from statistics import mean

from django.shortcuts import render
from django.views.generic import ListView
from base.models import Promotion, Grade


# Create your views here.

class UserPromotionList(ListView):
    model = Promotion
    context_object_name = "student_promotions"
    template_name = "promotions/index.html"
    promo = "promo"

    def get_context_data(self, **kwargs):
        context = super(UserPromotionList, self).get_context_data(**kwargs)
        grades = Grade.objects.filter(user=self.request.user)
        moy = {}
        for grade in grades:
            if grade.subject.id in moy:
                moy[grade.subject.id].append(grade.note)
            else:
                moy[grade.subject.id] = [grade.note]
        print(moy)
        context.update({
            'grades': list({"subject": g.subject, "note": g.note} for g in grades),
            'moy': [(k, sum(v) / len(v)) for k, v in moy.items()]
        })
        return context

    def get_queryset(self):
        return Promotion.objects.filter(users=self.request.user)
