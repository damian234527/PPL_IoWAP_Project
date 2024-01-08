from django.urls import path
from . import views

app_name = "files"
urlpatterns = [
    path("bethlehem/", views.index, name="main"),
    path("bethlehem/upload/", views.file_upload, name="file_upload"),
    path("bethlehem/download/<int:file_id>/", views.file_download, name="file_download"),
    path("bethlehem/fileslist/", views.files_list, name="files_list"),
]
