"""
from django import forms
from . import models


class PromptForm(forms.ModelForm):
    class Meta:
        model = models.Prompt
        fields = [""]
        widgets = {"date": forms.HiddenInput()}
"""
