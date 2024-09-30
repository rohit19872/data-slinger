from django.urls import path

from . import views, views_connect

urlpatterns = [
    path("", views.index, name="index"),
    path("event", views_connect.receive_event, name="receive_event"),
]