import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.utils import timezone
from django.http import HttpResponse
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


# 一覧表示
def index(request):
    todos = Todo.objects.all().order_by("due_date")
    filter_status = request.GET.get("filter")
    if filter_status == "incomplete":
        todos = todos.filter(is_completed=False)
    sort_by = request.GET.get("sort")
    if sort_by == "created":
        todos = todos.order_by("created_at")
    return render(request, "work09/index.html", {"todos": todos})


# 新規作成
def create(request):
    if request.method == "POST":
        title = request.POST.get("title", "no title")
        due_date = request.POST.get("due_date", timezone.now().date())
        Todo.objects.create(title=title, due_date=due_date)
        return redirect("work09:index")
    return render(request, "work09/create.html")


# 編集
def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "POST":
        todo.title = request.POST.get("title", todo.title)
        todo.due_date = request.POST.get("due_date", todo.due_date)
        todo.is_completed = "is_completed" in request.POST
        todo.save()
        return redirect("work09:index")
    return render(request, "work09/edit.html", {"todo": todo})


# 削除
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect("work09:index")


# 完了状態の切り替え
def toggle(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = not todo.is_completed  # 完了状態を反転
    todo.save()
    return redirect('work09:index')

# OPENAI テスト導入


def simple_qa_openai(request):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # query stringから質問を取得
    question = request.GET.get("question", "おすすめのレシピは？")
    prompt = "質問: {question}\n回答:".format(question=question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # または "gpt-4o" など
        messages=[{"role": "user", "content": prompt}],
    )
    return HttpResponse(f"<pre>{response.choices[0].message.content}</pre>")