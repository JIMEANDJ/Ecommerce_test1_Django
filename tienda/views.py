from django.shortcuts import render, get_object_or_404
from .models import Producto
from categorias.models import Categoria


# Create your views here.
def tienda(request, categoria_slug=None):
    categorias= None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug= categoria_slug)
        productos = Producto.objects.filter(categoria = categorias, is_avaliable=True)
        producto_count = productos.count()  
    else: 
        productos = Producto.objects.all().filter(is_avaliable=True).order_by('id')
        producto_count = productos.count()


    context= {
        'productos': productos,
        'producto_count' : producto_count
    }

    return render(request, 'tienda/tienda.html', context )

def detalles_producto(request,categoria_slug, producto_slug,):
    try:
        un_producto = Producto.objects.get(categoria__slug = categoria_slug, slug = producto_slug)

    except Exception as e:
        raise e 
    
    context = {
        'un_producto':un_producto,
    }
    return render(request, 'tienda/producto_detalles.html', context)