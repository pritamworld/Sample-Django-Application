from django.urls import path

from . import views

app_name = "boards"

urlpatterns = [
    #http://127.0.0.1:8000/
    path("", views.HomeView.as_view(), name="home"),
    #http://127.0.0.1:8000/poll/1
    path("poll/<int:poll_id>/", views.PollView.as_view(), name="poll"),
]