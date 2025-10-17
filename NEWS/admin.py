from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import News
from .models import Announcement

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_pinned")
    list_filter = ("is_pinned", "published_at")
    search_fields = ("title", "content",)


@admin.register(Announcement)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_pinned")
    list_filter = ("is_pinned", "published_at")
    search_fields = ("title", "content")