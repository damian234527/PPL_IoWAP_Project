from django.urls import path
from . import views

app_name = "help"
urlpatterns = [
    path("cana/", views.index, name="main"),
    path("cana/prompts/", views.prompts_list, name="prompts_list"),
]
