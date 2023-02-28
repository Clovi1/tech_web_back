from django.contrib import admin

from api.models import UserProfile, Tags, Posts


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ['date_create', 'date_update']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'views_count']
    search_fields = ['author', 'title']
