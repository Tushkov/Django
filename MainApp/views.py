from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import response
import json
from django.conf import settings
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
userData = {
        "surname": "Петров",
        "name": "Николай",
        "middlename": "Петрович",
        "phone": "8(923)600-0102",
        "email": "my_mail@mail.ru"
    }


# Create your views here.
def home(request):
    context = {
        "user" : userData
    }
 
    return render(request, "index.html", context)

def about(request):
    context = {
        "user" : userData
    }
 
    return render(request, "about.html", context)

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
