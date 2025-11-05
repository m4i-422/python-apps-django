from django.urls import path
from . import views


app_name = "work09"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:todo_id>/", views.edit, name="edit"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
    path("toggle/<int:todo_id>/", views.toggle, name="toggle"),
    # path("simple_qa/", views.simple_qa, name="simple_qa"),
]
