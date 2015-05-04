from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo_text', 'deadline', 'progress']
    fieldsets = [
        (None,               {'fields': ['todo_text']}),
    ]
admin.site.register(Todo)
# admin.site.register(Choice)
# Register your models here.
