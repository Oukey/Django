from django.shortcuts import render
import json, os
from .models import ProductCategory, Product

JSON_PATH = 'mainapp/json'


def loadMenuFromJSON():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as infile:
        return json.load(infile)


def main(request):
    title = 'главная'
    links_menu = loadMenuFromJSON()
    context = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/main.html', context)


def products(request):
    links_menu = loadMenuFromJSON()
    products = Product.objects.all()
    context = {'links_menu': links_menu, 'products': products}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html', context)
