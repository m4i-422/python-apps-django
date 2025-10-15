from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm


def index(request):
    memos = Memo.objects.all()
    return render(request, "work08/index.html", {"memos": memos})


def new(request):
    memo = Memo.objects.create()  # title は自動で "no title"
    return redirect("work08:edit", memo_id=memo.id)


def edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect("work08:index")
    else:
        form = MemoForm(instance=memo)

    return render(request, "work08/edit.html", {"form": form, "memo": memo})
