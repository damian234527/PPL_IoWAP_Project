from django.urls import path
from . import views

app_name = "help"
urlpatterns = [
    path("cana/", views.index, name="main"),
]