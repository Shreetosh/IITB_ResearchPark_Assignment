from django.urls import path
from . import views

urlpatterns = [
    path('', views.gen_invoice, name='generate_invoice'),
    #path('add_items', views.add_items, name='add_items'),
]


