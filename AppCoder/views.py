from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario, ClienteFormulario, CerveceriaFormulario, Clientes1Formulario
from AppCoder.models import Cerveceria, Producto, Cliente 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render

# Create your views here.

def inicioSesion(request):
    mensaje_error = ""  

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido, {user}"})
            else:
                mensaje_error = "Los datos ingresados son incorrectos. Por favor, inténtalo de nuevo."  
            mensaje_error = "Por favor, ingresa un nombre de usuario y contraseña válidos."  
    else:
        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario": form, "mensaje_error": mensaje_error})
    
def registro(request):
    if request.method=="POST":

       form = UserCreationForm(request.POST)

       if form.is_valid():

        username = form.cleaned_data["username"]
        form.save()
        return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario creado."})
    
    else:
        form = UserCreationForm()

    return render(request, "AppCoder/inicio.html", {"formulario":form})



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
        print("buscando")
        cerveceria = request.GET["cerveceria"]
        nombre_resultados = Cerveceria.objects.filter(nombre__iexact=cerveceria)

        return render(request, "AppCoder/cerveceria.html", {"cerveceria": cerveceria, "nombre": nombre_resultados})

    else:
        respuesta = "No se encuentran datos."

    return HttpResponse(respuesta)



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


def editarClientes(request, clienteUsuario):
    cliente = Cliente.objects.get(usuario=clienteUsuario)

    if request.method == "POST":

        formulario2 = Clientes1Formulario(
            request.POST, initial={"usuario": cliente.usuario, "cliente": cliente.cliente})

        if formulario2.is_valid():
            info = formulario2.cleaned_data
            cliente.cliente = info["cliente"]
            cliente.usuario = info["usuario"]
            cliente.save()
            return render(request, "AppCoder/inicio.html")

    else:
        formulario2 = Clientes1Formulario(
            initial={"usuario": cliente.usuario, "cliente": cliente.cliente})

    return render(request, "AppCoder/editarClientes.html", {"form2": formulario2, "cliente": clienteUsuario})


##---------------------------

class ListaProducto (ListView):

    model = Producto

class DetalleProducto (DetailView):

    model = Producto

class CrearProducto (CreateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ["nombre", "marca", "precio"]

class ActualizarProducto (UpdateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ["nombre", "marca", "precio"]

class BorrarProducto (DeleteView):
    model = Producto
    success_url = "/AppCoder/producto/list"   








