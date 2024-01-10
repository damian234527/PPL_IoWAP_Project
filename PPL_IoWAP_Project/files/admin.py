from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'date', 'ip')


admin.site.register(File, FileAdmin)
