from django.shortcuts import render
from dotenv import load_dotenv
import os
# Create your views here.


def index(request):
    load_dotenv()
    return render(request, "help/index.html")
