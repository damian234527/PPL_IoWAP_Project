from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.welcome_page, name="welcome"),
    path("jerusalem/", views.home_page, name="main"),
]
