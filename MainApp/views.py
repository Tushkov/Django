from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import response
import json
from Django import settings
from MainApp.models import Work, Item, Country

file = open(settings.BASE_DIR / "country.json")
data = json.load(file)
file.close()

for item in data:
    country = Country(country=item["country"], languages=1)


# Create a JSON data dictionary
country =  {
        "country": "Aruba",
        "languages": [
            "Dutch",
            "English",
            "Papiamento",
            "Spanish"
        ]
    }





             
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

def countries_list_db(request):
    context = {
        "items" : data
    }

    return render(request, "countries_list_db.html", context)

def country_db(request, country):
    for item in data:
        if country == item["country"]:
            context = {
                "item" : item
            }
    
    return render(request, "country_db.html", context)

def work(request):
    context = {
        "work" : Work.objects.all()
    }
    
    return render(request, "work.html", context)

def reload_db(request):
    db = country()
    
    context = {
        "work" : Work.objects.all()
    }
    
    return render(request, "countries_list_db.html", context)

def items(request):
    items = Item.objects.all()
    
    context = {
        "items" : items
    }
    
    return render(request, "items.html", context)

def item_id(request, id):
    try:
        item = Item.objects.get(id=id)
    except "ObjectDoesNotFound":
        return HttpResponseNotFound(f"Товар ID = {id} не найден")
    else:
        context = {
            "item" : item
        }
    
    return render(request, "item.html", context)
