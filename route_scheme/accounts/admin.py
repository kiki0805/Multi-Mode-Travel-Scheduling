from django.contrib import admin
from accounts.models import UserProfile, UserStatus


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'location', 'count')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserStatus, UserStatusAdmin)
