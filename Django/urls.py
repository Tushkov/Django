from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('work', views.work, name="work"),
    path('countries_list', views.countries_list, name="countries-list"),
    path('country/<country>', views.country, name="countryj-detail"),
    path('countries_list_db', views.countries_list_db, name="countries-list-db"),
    path('country_db/<country>', views.country_db, name="country-detail"),
    path('items', views.items, name="items-list"),
    path('item/<int:id>', views.item_id, name="item-detail"),

]
