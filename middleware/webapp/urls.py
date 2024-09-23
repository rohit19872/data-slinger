from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("event", views.receive_event, name="receive_event"),
]