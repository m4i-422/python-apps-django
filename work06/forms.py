from django import forms


# 令和年変換用フォーム
class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(label="令和年")


# BMI用フォーム
class BmiForm(forms.Form):
    height = forms.FloatField(label="身長(cm)")
    weight = forms.FloatField(label="体重(kg)")


# 割り勘用フォーム
class WarikanForm(forms.Form):
    total = forms.FloatField(label="合計金額")
    people = forms.IntegerField(label="人数")


# 貯金シミュレーション用フォーム
class ChokinForm(forms.Form):
    monthly = forms.FloatField(label="毎月の貯金額")
    interest = forms.FloatField(label="年利(%)", initial=0)
    years = forms.IntegerField(label="何年後")


# 四則演算計算機フォーム
class CalculatorForm(forms.Form):
    a = forms.FloatField(label="数字1")
    b = forms.FloatField(label="数字2")
    operator = forms.ChoiceField(
        choices=[("+", "+"), ("-", "-"), ("*", "*"), ("/", "/")],
        label="演算"
    )
