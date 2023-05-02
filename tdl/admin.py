from django.contrib import admin
# models.py ထဲက Task Class ကို Import လုပ်မယ်။
from .models import Task

# Task ကို Admin Panel မှာ ပြဖို့ 
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

# admin panel မှာ Task model ကို ထည့်မယ်။
# admin.site.register(Task)
admin.site.register(Task, TaskAdmin)