from django.contrib import admin

# Register your models here.
from .models import Exam, Question


@admin.register(Exam)
class AdminExam(admin.ModelAdmin):
    pass


@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    pass
