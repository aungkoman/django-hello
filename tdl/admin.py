from django.contrib import admin
# models.py ထဲက Task Class ကို Import လုပ်မယ်။
from .models import Task, Student

# update heading and title
admin.site.site_header = "To Do List"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "To Do List"

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','marks', 'grade', 'result')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')


admin.site.register(Task, TaskAdmin)
admin.site.register(Student, StudentAdmin)























# update title
"""
admin.site.site_header = "To Do List"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "To Do List"

# Task ကို Admin Panel မှာ ပြဖို့ 
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

# admin panel မှာ Task model ကို ထည့်မယ်။
# admin.site.register(Task)
admin.site.register(Task, TaskAdmin)

admin.site.register(Student)
"""