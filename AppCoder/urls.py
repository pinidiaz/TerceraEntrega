from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cerveceria/", cerveceria, name="Cerveceria"),
    path("producto/", producto, name="Producto"),
    path("cliente/", cliente, name="Cliente"),  
    path("productoFormulario/", productoFormulario, name="FormularioProducto"),
    path("buscarProducto/", busquedaProducto, name="BuscarProducto"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("clienteFormulario/", clienteFormulario, name="FormularioCliente"),
    path("cerveceriaFormulario/", cerveceriaFormulario, name="FormularioCerveceria"),
    path("buscarCliente/", busquedaCliente, name="BuscarCliente"),
    path("buscar/", buscar, name="BuscarCliente"),
    path("buscar2/", buscar2, name="BuscarCerveceria"),
    path("login", inicioSesion, name="Login"),
    path("register", registro, name="Registro"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),



    #CRUD DE CLIENTES
    path("leerClientes/", leerClientes, name="ClientesLeer"),
    path("crearClientes/", crearClientes, name="ClientesCrear"),
    path("eliminarClientes/<clienteUsuario>/", eliminarClientes, name="EliminarClientes"),
    path("editarClientes/<clienteUsuario>/", editarClientes, name="EditarClientes"),


    #CRUD DE PRODUCTOS
    path("producto/list", ListaProducto.as_view(), name="ProductosLista"),
    path("producto/<int:pk>", DetalleProducto.as_view(), name="ProductosDetalle"),

    path("leerProducto/", leerProducto, name="ProdcutoLeer"),
    path("crearProducto/", crearProducto, name="ProductoCrear"),
    path("eliminarProducto/<productoNombre>/", eliminarProducto, name="EliminarProducto"),
    path("editarProducto/<productoNombre>/", editarProducto, name="EditarProducto"),

]   

