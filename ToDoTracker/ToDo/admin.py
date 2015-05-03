from django.contrib import admin

from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'pub_date', 'was_published_recently']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
# Register your models here.
