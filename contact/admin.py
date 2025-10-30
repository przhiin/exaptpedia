from django.contrib import admin
from .models import contact

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'name', 'position', 'email', 'phone')
    list_filter = ('occupation_category',)
    search_fields = ('name', 'email', 'phone', 'occupation')
