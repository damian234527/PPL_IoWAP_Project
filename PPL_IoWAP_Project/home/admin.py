from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'creator', 'date', 'ip')


admin.site.register(Message, MessageAdmin)
