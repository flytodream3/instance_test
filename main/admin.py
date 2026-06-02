from django.contrib import admin

from .models import Shelf, Product


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'shelf', 'category', 'quantity']