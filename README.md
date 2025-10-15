# python-apps-django


起動方法 python manage.py runserver

止め方 Control コマンド と C の同時押し

新しいアプリケーションを作る↓

ターミナルに入力 ↓

python manage.py startapp "アプリケーション名"


プロジェクト / settings.py / INSTALLED_APPSにアプリケーション名を追加


プロジェクト / urls.py / urlpatternsに

path('work05/', include('work05.urls'))

のように追加する