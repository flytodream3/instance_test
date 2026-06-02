from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.get_shelves, name='home'),
    path('shelf/<shelf_id>', views.get_shelf, name='shelf'),
    path('shelf/<shelf_id>/add', views.add_to_shelf, name='add_to_shelf'),
]