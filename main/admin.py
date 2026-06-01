from django.contrib import admin

from .models import Shelf, Product


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['name']
