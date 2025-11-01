from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Members, JobCategory


class DynamicOccupationCategoryFilter(admin.SimpleListFilter):
    title = 'Occupation Category'
    parameter_name = 'occupation_category'

    def lookups(self, request, model_admin):
        categories = JobCategory.objects.all().order_by('name')
        return [(cat.id, cat.name) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(occupation_category_id=self.value())
        return queryset


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('profile_image_tag', 'name', 'position', 'email', 'phone')
    search_fields = ('name', 'email', 'phone', 'position', 'occupation_category__name')
    list_filter = (DynamicOccupationCategoryFilter,)

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                obj.profile_image.url
            )
        return "-"
    profile_image_tag.short_description = 'Profile Image'

    actions = ['delete_selected_users']

    def delete_selected_users(self, request, queryset):
        count = queryset.count()
        for user in queryset:
            if user.profile_image and user.profile_image.name != 'user_images/default.png':
                user.profile_image.delete(save=False)
            user.delete()
        self.message_user(request, f"Successfully deleted {count} user(s).", messages.SUCCESS)
    delete_selected_users.short_description = "Delete selected users (with cleanup)"


# ✅ DO NOT replace the global admin.site
# Just extend its context safely
def custom_index(self, request, extra_context=None):
    total_members = Members.objects.count()
    print("✅ custom_index called — total_members =", total_members)
    if extra_context is None:
        extra_context = {}
    extra_context['total_members'] = total_members
    return admin.sites.AdminSite.index(self, request, extra_context=extra_context)

# Monkey-patch the index method safely
admin.site.index = custom_index.__get__(admin.site, admin.sites.AdminSite)
