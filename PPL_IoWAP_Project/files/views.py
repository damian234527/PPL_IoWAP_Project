from django.shortcuts import render
from .models import File
from . import forms
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "files/index.html")


def files_list(request):
    files = File.objects.all().order_by('-date')
    return render(request, "files/files_list.html", {"files": files})


def file_upload(request):
    if request.method == "POST":
        file_form = forms.FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            new_file = file_form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                new_file.ip = x_forwarded_for.split(',')[0]
            else:
                new_file.ip = request.META.get('REMOTE_ADDR')
            new_file.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'file_list_changed'})
    else:
        file_form = forms.FileForm()
    return render(request, "files/file_upload.html", {"file_form": file_form})





def file_download(request, file_id):
    file_to_download = File.objects.get(pk=file_id)
    response = HttpResponse(file_to_download.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{file_to_download.file.name}"'
    return response
