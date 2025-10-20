from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('profile_image_tag', 'name', 'occupation', 'email', 'phone')

    def profile_image_tag(self, obj):
        if obj.profile_image:
            # Display the image as a small thumbnail (40x40)
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                obj.profile_image.url
            )
        return "-"
    
    profile_image_tag.short_description = 'Profile Image'
    profile_image_tag.allow_tags = True

# Register your model with the admin
admin.site.register(CustomUser, RegisterAdmin)


# Register your models here.
