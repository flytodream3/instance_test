from django.shortcuts import render, get_object_or_404, redirect

from. models import Shelf, Product
from .forms import AssignShelfFormSet

def get_shelves(request):
    shelves = Shelf.objects.all()
    context = {
        'title': 'Shelves',
        'shelves': shelves,
    }
    return render(request, 'main/shelves.html', context)

def get_shelf(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id)
    products = shelf.products.all()
    context = {
        'title': shelf.name,
        'shelf': shelf,
        'products': products,
    }
    return render(request, 'main/shelf.html', context)

def add_to_shelf(request, shelf_id):
    shelf = get_object_or_404(Shelf, id=shelf_id)
    products = Product.objects.order_by('name')

    if request.method != 'POST':
        formset = AssignShelfFormSet()
    else:
        formset = AssignShelfFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    product_id = form.cleaned_data['product_id']
                    if product_id:
                        try:
                            product = Product.objects.get(id=product_id)
                            if product.shelf != shelf:
                                product.shelf = shelf
                                product.save()
                        except Product.DoesNotExist:
                            pass
            return redirect('main:shelf', shelf_id=shelf.id)

    context = {
        'title': 'Add to shelf',
        'formset': formset,
        'shelf': shelf,
        'products': products,
    }
    return render(request, 'main/add_to_shelf.html', context)
