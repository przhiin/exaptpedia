from django.contrib import admin

# Register your models here.
# community/admin.py
from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
