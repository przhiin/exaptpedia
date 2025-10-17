from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "created_at")
    search_fields = ("title", "description")
    list_filter = ("date",)
