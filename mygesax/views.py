from statistics import mean

from django.shortcuts import render
from django.views.generic import ListView
from base.models import Promotion, Grade, Promotion, Subject
from django.views import generic
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required 

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

class HomeView(generic.CreateView):
    template_name = 'home.html'
    model = User
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fs = FileSystemStorage()
        files = fs.listdir('static/uploads')
        context["uploaded_file_url"] = files[1]
        return context
    
    def get_queryset(self):
        return self.request.user

class TeacherClassList(ListView):
    model = Subject 
    context_object_name="teacher_trombi"
    template_name="promotions/class.html"
    def get_queryset(self):
        return Subject.objects.filter(teacher=self.request.user.teacher)

class PromoList(ListView):
    model = Promotion    
    context_object_name="student_promotion"
    template_name="promotions/promo.html"
    def get_queryset(self):
        return Promotion.objects.filter(name=self.kwargs['name'])
