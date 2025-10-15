from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="work07_index"),
    path("omikuji/", views.omikuji, name="omikuji"),
    path("janken/", views.janken, name="janken"),
    path("hilow/", views.hilow, name="hilow"),
]
