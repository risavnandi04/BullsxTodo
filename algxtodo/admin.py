from django.contrib import admin
from .models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "due_date")
    list_filter = ("status",)
    search_fields = ("title", "description")
    fieldsets = (
        (None, {"fields": ("title", "description", "status")}),
        (
            "Advanced options",
            {
                "classes": ("collapse",),
                "fields": ("due_date", "tags"),
            },
        ),
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
