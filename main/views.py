from django.shortcuts import render

from. models import Shelf, Product

def get_shelves(request):
    shelves = Shelf.objects.all()
    context = {
        'title': 'Shelves',
        'shelves': shelves,
    }
    return render(request, 'main/shelves.html', context)