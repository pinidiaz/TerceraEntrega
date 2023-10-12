from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario, ClienteFormulario, CerveceriaFormulario, Clientes1Formulario
from AppCoder.models import Cerveceria, Producto, Cliente 

 

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cerveceria(request):
    return render(request,"AppCoder/cerveceria.html")
  
def producto(request):   
    return render(request,"AppCoder/producto.html")

def cliente(request): 
    return render(request,"AppCoder/cliente.html")
    
##-------------------

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

        return render(request, "AppCoder/producto.html", {"producto":producto, "nombre":nombre_resultados})
    
    else:
        respuesta = "No se encuentran datos."
    
    return HttpResponse (respuesta)



#-----------------------

def clienteFormulario(request):

    if request.method == "POST":

        formulario2 = ClienteFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data
            cliente = Cliente(cliente=info["cliente"], usuario=info["usuario"])
        
            cliente.save()

        return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = ClienteFormulario()

    return render(request, "AppCoder/clientes1Formulario.html",{"form2":formulario2 })


def busquedaCliente(request):

    return render(request, "AppCoder/inicio.html")



def buscar(request):

    if "cliente" in request.GET:
        
        cliente = request.GET["cliente"]
        usuario_resultados = Cliente.objects.filter(usuario__iexact=cliente)

        return render(request, "AppCoder/cliente.html", {"cliente":cliente, "usuario":usuario_resultados})
    
    else:
        respuesta = "No se encuentran datos."
    
    return HttpResponse (respuesta)



#--------------------------

def cerveceriaFormulario(request):

    if request.method == "POST":

        formulario3 = CerveceriaFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data
            cerveceria = Cerveceria(nombre=info["nombre"], ciudad=info["ciudad"], direccion=info["direccion"])
        
            cerveceria.save()

        return render(request, "AppCoder/inicio.html")

    else:

        formulario3 = CerveceriaFormulario()

    return render(request, "AppCoder/cerveceriaFormulario.html",{"form3":formulario3})


def busquedaCerveceria(request):

    return render(request, "AppCoder/inicio.html")



def buscar2(request):

    if "cerveceria" in request.GET:
        
        nombre = request.GET["nombre"]
        nombre_resultados = Cerveceria.objects.filter(nombre__iexact=cerveceria)

        return render(request, "AppCoder/cerveceria.html", {"cerveceria":cerveceria, "nombre":nombre_resultados})
    
    else:
        respuesta = "No se encuentran datos."
    
    return HttpResponse (respuesta)



##-----------------------------
 
def leerClientes(request):

    clientes = Cliente.objects.all()

    contexto = {"customer": clientes}

    return render(request, "AppCoder/leerClientes.html", contexto)


def crearClientes(request):
    if request.method == "POST":

        formulario2 = Clientes1Formulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data
            cliente = Cliente(cliente=info["cliente"], usuario=info["usuario"])
        
            cliente.save()

        return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = Clientes1Formulario()

    return render(request, "AppCoder/clientes1Formulario.html",{"form2":formulario2 })


def eliminarClientes(request,clienteUsuario):
    cliente = Cliente.objects.get(usuario=clienteUsuario)
    cliente.delete()

    clientes = Cliente.objects.all()
    contexto = {"customer":clientes}

    return render(request, "AppCoder/leerClientes.html", contexto)


def editarClientes(request,clienteUsuario):
    cliente = Cliente.objects.get(usuario=clienteUsuario)

    if request.method == "POST":
       
       if formulario2.is_valid():

            info = formulario2.cleaned_data

            cliente.cliente = info["cliente"]
            cliente.usuario = info["usuario"]
        
            cliente.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        formulario2 = Clientes1Formulario(inital={"usuario":cliente.usuario, "cliente":cliente.cliente})

    return render(request, "AppCoder/editarFormulario.html",{"form2":formulario2,"cliente":clienteUsuario})





