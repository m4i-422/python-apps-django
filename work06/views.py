from django.shortcuts import render
from .forms import ReiwaForm, BmiForm, WarikanForm, ChokinForm, CalculatorForm


def index(request):
    return render(request, "work06/index.html")


def reiwa(request):
    result = None

    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            result = reiwa_year + 2018

    else:
        form = ReiwaForm()

    return render(request, "work06/reiwa.html",
                  {"form": form, "result": result})


def bmi(request):
    result = None
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            h = form.cleaned_data["height"] / 100
            w = form.cleaned_data["weight"]
            result = round(w / (h*h), 2)
    else:
        form = BmiForm()
    return render(request, "work06/bmi.html", {"form": form, "result": result})


def warikan(request):
    result = None
    if request.method == "POST":
        form = WarikanForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data["total"]
            people = form.cleaned_data["people"]
            if people > 0:
                result = round(total / people, 2)
    else:
        form = WarikanForm()
    return render(request, "work06/warikan.html",
                  {"form": form, "result": result})


def chokin(request):
    result = None
    if request.method == "POST":
        form = ChokinForm(request.POST)
        if form.is_valid():
            monthly = form.cleaned_data["monthly"]
            interest = form.cleaned_data["interest"]/100
            years = form.cleaned_data["years"]
            total = 0
            history = []
            for y in range(1, years+1):
                total = total * (1 + interest) + monthly*12
                history.append((y, round(total, 2)))
            result = history
    else:
        form = ChokinForm()
    return render(request, "work06/chokin.html",
                  {"form": form, "result": result})


def calculator(request):
    result = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            op = form.cleaned_data["operator"]
            try:
                result = eval(f"{a}{op}{b}")
            except ZeroDivisionError:
                result = "割り算で0は不可"
    else:
        form = CalculatorForm()
    return render(request, "work06/calculator.html",
                  {"form": form, "result": result})
