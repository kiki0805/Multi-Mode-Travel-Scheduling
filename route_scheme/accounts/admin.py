# -*- coding: utf-8 -*-
from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'location_count')


admin.site.register(UserProfile, UserProfileAdmin)
