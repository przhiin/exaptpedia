from django.contrib import admin
from django.utils.html import format_html
from .models import contact

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('profile_image_tag', 'name', 'position', 'email', 'phone')
    list_filter = ('occupation_category',)
    search_fields = ('name', 'email', 'phone', 'occupation_category')

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%; object-fit:cover;" />',
                obj.profile_image.url
            )
        return "-"
    profile_image_tag.short_description = 'Profile Image'
