from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import response
import json
from Django import settings
from .models import Work

file = open(settings.BASE_DIR / "country-by-languages.json")
data = json.load(file)
file.close()

             
# Create your views here.
def home(request):
    # text = """
    # <h1>"Изучаем django День первый !"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # <h2><a href="/about">About</a></h2>
    # <h2><a href="/items">Items<a></h2>
    # """
    # return HttpResponse(text)
    context = {
        "name": "Петров Николай Петрович",
        "email": "my_mail@mail.ru"
    }

    return render(request, "index.html", context)

def countries_list(request):
    context = {
        "items" : data
    }

    return render(request, "countries_list.html", context)

def country(request, country):
    for item in data:
        if country == item["country"]:
            context = {
                "item" : item
            }
    
    return render(request, "country.html", context)

def work(request):
    context = {
        "work" : Work.objects.all()
    }
    
    return render(request, "work.html", context)
