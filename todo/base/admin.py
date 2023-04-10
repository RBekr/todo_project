from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('created', )
    sortable_by = ('created')

admin.site.register(Task, TaskAdmin)
