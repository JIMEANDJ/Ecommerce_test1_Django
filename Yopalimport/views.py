from django.shortcuts import render
from tienda.models import Producto

def home(request):
    productos = Producto.objects.all().filter(is_avaliable=True)
    producto_count = productos.count()
    context= {
        'productos': productos,
        'producto_count' : producto_count,
    }
    return render(request, 'home.html', context)
