from django.urls import path
from . import views

# Namespace para la aplicación de productos
app_name = 'productos'

# Definición de las URL de la aplicación
urlpatterns = [
    path('articulos/', views.lista_articulos, name='lista_articulos'),
    path('carrito/', views.carrito, name='carrito'),  
    path('contacto/', views.contacto, name='contacto'),
    path('', views.home, name='home'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
