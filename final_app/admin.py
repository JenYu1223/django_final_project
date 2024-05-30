from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, UserProfile
from final_app import models

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_username', 'preferences', 'suggested_course_id', 'recently_viewed_course_id')
    search_fields = ('user__email', 'user__username')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Username'

admin.site.register(UserProfile, UserProfileAdmin)
    
