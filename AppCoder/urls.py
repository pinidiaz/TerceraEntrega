from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cerveceria/", cerveceria, name="Cerveceria"),
    path("producto/", producto, name="Producto"),
    path("pedido/", pedido, name="Pedido"),  
    path("productoFormulario/", productoFormulario, name="FormularioProducto"),
    path("buscarProducto/", busquedaProducto, name="BuscarProducto"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    
]
