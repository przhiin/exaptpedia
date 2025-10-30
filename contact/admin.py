from django.contrib import admin
from .models import contact

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_doctor', 'occupation')
    list_filter = ('is_doctor',)
    search_fields = ('name', 'email', 'phone', 'occupation')
