@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "is_completed", "scheduled_time")
    list_filter = ("is_completed",)
    search_fields = ("title",)
