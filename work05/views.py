from django.shortcuts import render


# Create your views here.
def index(request):
    name = "mai"
    name_en = "Kaneko Mai"
    birth_year = 2009

    return render(
        request,
        "work05/index.html",
        {
            "name": name,
            "name_en": name_en,
            "birth_year": birth_year,
        },
    )
