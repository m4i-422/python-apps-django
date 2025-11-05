from django.urls import path
from . import views

app_name = "work08"

urlpatterns = [
    path("", views.index, name="index"),        # メモ一覧
    path("edit/<int:memo_id>/", views.edit, name="edit"),  # 編集画面
    path("new/", views.new, name="new"),        # 新規作成
]
