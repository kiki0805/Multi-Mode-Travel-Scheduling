from django.contrib import admin
from mode.models import Mode
# Register your models here.

class ModeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'extra_fields')

admin.site.register(Mode, ModeAdmin)
