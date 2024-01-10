from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Producto, Cliente, ItemCarrito
from .forms import BuscarForm, CarritoForm, ContactoForm

# Vista para la página principal
def home(request):
    return render(request, 'productos/home.html')

# Vista para la lista de artículos disponibles
def lista_articulos(request):
    # Filtra los productos disponibles y ordénalos por nombre
    articulos = Producto.objects.filter(disponible=True).order_by('nombre')
    return render(request, 'productos/lista_articulos.html', {'articulos': articulos})

# Vista para el carrito de compras
def carrito(request):
    if request.user.is_authenticated:
        cliente = get_object_or_404(Cliente, id=request.user.id)
        carrito = cliente.carrito.all()
        total_carrito = sum(item.subtotal() for item in carrito)
    else:
        carrito = []
        total_carrito = 0

    contexto = {'carrito': carrito, 'total_carrito': total_carrito}
    return render(request, 'productos/carrito.html', contexto)

# Vista para la página de contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario si es válido
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            motivo = form.cleaned_data['motivo']
            comentarios = form.cleaned_data['comentarios']
            
            # Aquí podrías realizar acciones adicionales con los datos del formulario

    else:
        form = ContactoForm()

    contexto = {'form': form}
    return render(request, 'productos/contacto.html', contexto)

# Vista para agregar un producto al carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id, disponible=True)

    if request.user.is_authenticated:
        cliente, creado = Cliente.objects.get_or_create(email=request.user.email)
        item_carrito, creado = ItemCarrito.objects.get_or_create(producto=producto, cliente=cliente)
        item_carrito.cantidad += 1
        item_carrito.save()

    # Utiliza reverse para obtener la URL de 'lista_articulos'
    lista_articulos_url = reverse('productos:lista_articulos')
    return redirect(lista_articulos_url)

# Vista para eliminar un ítem del carrito
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('carrito')
