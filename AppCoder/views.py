from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario
from AppCoder.models import Cerveceria, Producto, Pedido



# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cerveceria(request):
    return render(request,"AppCoder/cerveceria.html")
  
def producto(request):   
    return render(request,"AppCoder/producto.html")

def pedido(request): 
    return render(request,"AppCoder/pedido.html")

def productoFormulario(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre", "")

        marca = request.POST.get("marca", "")

        nuevo_producto = Producto(nombre=nombre, marca=marca)
        nuevo_producto.save()

        formulario1 = ProductoFormulario(request.POST)  

        if formulario1.is_valid():
            info = formulario1.cleaned_data

            nuevo_producto = Producto(nombre=info["nombre"],marca=info["marca"])
        
            nuevo_producto.save()
        
            return render(request, "AppCoder/inicio.html")
        
    else:

        formulario1 = ProductoFormulario()
    

    return render(request, "AppCoder/productoFormulario.html", {"form1":formulario1})




def busquedaProducto(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if "producto" in request.GET:
        
        producto = request.GET["producto"]
        nombre_resultados = Producto.objects.filter(nombre__iexact=producto)

        return render(request, "AppCoder/inicio.html", {"producto":producto, "nombre":nombre_resultados})
    
    else:
        respuesta = "No se encuentran datos."
    
    return HttpResponse (respuesta)
