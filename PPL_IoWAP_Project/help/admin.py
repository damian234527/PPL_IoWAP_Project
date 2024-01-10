from django.contrib import admin
from .models import Prompt, Answer


class PromptAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'date', 'ip')


admin.site.register(Prompt, PromptAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'reference', 'question')


admin.site.register(Answer, AnswerAdmin)
