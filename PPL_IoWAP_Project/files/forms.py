from django import forms
from . import models


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = ["name", "description", "file"]
        widgets = {"date": forms.HiddenInput()}
