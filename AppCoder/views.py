from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import Cerveceria, Producto, Cliente 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

       form = UsuarioRegistro(request.POST)

       if form.is_valid():

        username = form.cleaned_data["username"]
        form.save()
        return redirect("Inicio")
    
    else:
        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario":form})

@login_required
def editarUsuario(request):
    usuario = request.user

    if request.method == "POST":
        form = FormularioEditar(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })
    
    return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario": usuario})
#-------------------------------

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


def leerProducto(request):
    
    producto = Producto.objects.all()
    contexto ={"product": producto}

    return render(request, "AppCoder/leerProducto.html", contexto)


def crearProducto(request):
    if request.method == "POST":
        miFormulario = ProductoFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            nombre = info["nombre"]
            marca = info["marca"]
            precio = info["precio"]

            producto = Producto(nombre=nombre, marca=marca, precio=precio)

            producto.save()

            producto.save()

            return render(request, "AppCoder/inicio.html")
        
    else: 
        miFormulario = ProductoFormulario()
    
    return render(request, "AppCoder/productoFormulario.html", {"miFormulario":miFormulario})


def eliminarProducto(request,productoNombre):

    producto = Producto.objects.get(nombre=productoNombre)
    producto.delete()

    producto = Producto.objects.all()
    contexto = {"product":producto}

    return render(request, "AppCoder/leerProducto.html",contexto)

def editarProducto(request,productoNombre):
    producto = Producto.objects.get(nombre=productoNombre)

    if request.method == "POST":
        miFormulario = ProductoFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            producto.nombre = info["nombre"]
            producto.marca = info["marca"]
            producto.precio = info["precio"]

            producto.save()


            return render(request, "AppCoder/inicio.html")
        
    else: 
        miFormulario = ProductoFormulario(initial={"nombre":producto.nombre, "marca":producto.marca, 
        "precio":producto.precio})
    
    return render(request, "AppCoder/editarProducto.html", {"miFormulario":miFormulario, "nombre":productoNombre})



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

@login_required
def busquedaCliente(request):

    return render(request, "AppCoder/inicio.html")


@login_required
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

@login_required
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


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario": form})
    
    
    ##---------------------------

class ListaProducto (LoginRequiredMixin, ListView):

    model = Producto

class DetalleProducto (LoginRequiredMixin, DetailView):

    model = Producto

class CrearProducto (LoginRequiredMixin, CreateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ["nombre", "marca", "precio"]

class ActualizarProducto (LoginRequiredMixin, UpdateView):

    model = Producto
    success_url = "/AppCoder/producto/list"
    fields = ["nombre", "marca", "precio"]

class BorrarProducto (LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = "/AppCoder/producto/list"   






