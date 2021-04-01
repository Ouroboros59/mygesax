from django.contrib import admin
from . import models
from base.models import Subject, Grade, Promotion

admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Promotion)
