from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('work', views.work),
    path('countries_list', views.countries_list),
    path('country/<country>', views.country),
    path('countries_list_db', views.countries_list_db),
    path('country_db/<country>', views.country_db),
    path('items', views.items),
    path('item/<int:id>', views.item_id),

]
