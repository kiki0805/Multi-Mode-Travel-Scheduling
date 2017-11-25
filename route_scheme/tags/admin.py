from django.contrib import admin
from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Tag, TagAdmin)
