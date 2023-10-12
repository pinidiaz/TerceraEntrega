from django.urls import path
from AppCoder.views import *

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


    #CRUD DE CLIENTES
    path("leerClientes/", leerClientes, name="ClientesLeer"),
    path("crearClientes/", crearClientes, name="ClientesCrear"),
    path("eliminarClientes/<clienteUsuario>/", eliminarClientes, name="EliminarClientes"),
    path("editarClientes/<clienteUsuario>/", editarClientes, name="EditarClientes"),

] 
