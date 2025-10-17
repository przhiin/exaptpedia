from django.contrib import admin
from . models import CustomUser

class RegisterAdmin(admin.ModelAdmin):
    list_display=('name','occupation','email', 'phone')


# Register your models here.
admin.site.register(CustomUser, RegisterAdmin)