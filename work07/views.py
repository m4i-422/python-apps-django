from django.shortcuts import render
import random


# トップページ
def index(request):
    return render(request, "work07/index.html")


# おみくじ
def omikuji(request):
    result = None
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

    if "draw" in request.GET:
        result = random.choice(fortunes)

    return render(
        request,
        "work07/omikuji.html",
        {"result": result}
    )


# じゃんけん
def janken(request):
    player = request.GET.get("player")
    cpu_choice = None
    result = None
    hands = ["グー", "チョキ", "パー"]

    if player:
        cpu_choice = random.choice(hands)
        # 勝敗判定
        if player == cpu_choice:
            result = "あいこ"
        elif (
            (player == "グー" and cpu_choice == "チョキ")
            or (player == "チョキ" and cpu_choice == "パー")
            or (player == "パー" and cpu_choice == "グー")
        ):
            result = "勝ち"
        else:
            result = "負け"

    return render(
        request,
        "work07/janken.html",
        {"cpu_choice": cpu_choice, "result": result}
    )


# Hi & Low
def hilow(request):
    previous_number = request.session.get("previous_number")
    next_number = None
    result = None

    # 最初の数字を設定
    if not previous_number:
        previous_number = random.randint(1, 13)
        request.session["previous_number"] = previous_number

    # プレイヤーが選択した場合
    choice = request.GET.get("choice")
    if choice:
        next_number = random.randint(1, 13)
        if (choice == "high" and next_number > previous_number) or (
            choice == "low" and next_number < previous_number
        ):
            result = "当たり！"
        elif next_number == previous_number:
            result = "あいこ！"
        else:
            result = "外れ…"
        # 次回用に更新
        request.session["previous_number"] = next_number
        previous_number = previous_number  # 表示用

    return render(
        request,
        "work07/hilow.html",
        {
            "previous_number": previous_number,
            "next_number": next_number,
            "result": result,
        },
    )
