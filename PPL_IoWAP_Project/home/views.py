from django.shortcuts import render, redirect
from .models import Message
from . import forms
from datetime import datetime

def welcome_page(request):
    return render(request, "home/welcome_page.html")


def home_page(request):
    messages = Message.objects.all()
    if request.method == "POST":
        new_message_form = forms.MessageForm(request.POST)
        if new_message_form.is_valid():
            new_message = new_message_form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                new_message.ip = x_forwarded_for.split(',')[0]
            else:
                new_message.ip = request.META.get('REMOTE_ADDR')
            new_message.save()
    else:
        new_message_form = forms.MessageForm()
    return render(request, "home/home_page.html", {"messages": messages, "new_message_form": new_message_form})