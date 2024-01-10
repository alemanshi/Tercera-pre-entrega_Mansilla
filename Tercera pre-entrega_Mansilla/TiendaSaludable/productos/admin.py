from django.contrib import admin
from .models import Producto, Cliente, ItemCarrito, Categoria

# Registra los modelos en la interfaz de administración de Django

# Registro del modelo Producto
admin.site.register(Producto)

# Registro del modelo Cliente
admin.site.register(Cliente)

# Registro del modelo ItemCarrito
admin.site.register(ItemCarrito)

# Registro del modelo Categoria
admin.site.register(Categoria)
