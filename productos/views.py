from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from django.template import loader
# Create your views here.

def user(request):
    return render(request, 'web/usuario.html')

def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'web/index.html', {'categorias': categorias})

def categoria(request):
    categorias = Categoria.objects.get(id=categoria_id)
    categoria_estaticas = [
        {        
        "categoria1" : "Computacion",
        "imagen1" : "img/computacion.jpg",
    },
      {        
        "categoria2" : "Consolas",
        "imagen2" : "img/computacion.jpg",
    },
      {        
        "categoria3" : "Videojuegos",
        "imagen3" : "img/computacion.jpg",
    },

    ]
    categorias = Categoria.objects.all()

    return render(request, 'web/index.html', {'categorias': categorias, 'categorias_estaticas': categorias_estaticas})
    
def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'web/productos.html', {'categoria': categoria, 'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'web/detalle.html', {'producto': producto})

