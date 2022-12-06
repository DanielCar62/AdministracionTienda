from django.urls import path

from .views import cambiar_contrasenia, contacto, ResultadoBusquedaAmplificador, buscar_amplificador, ResultadoBusquedaProveedor, buscar_proveedor, inicioAmplificador, inicioInstrumento, inicioProveedor, ResultadoBusquedaInstrumento, buscar_instrumento, about, editarProveedor, editarPerfil, register, loginView, editarAmplificador, editarInstrumento, eliminarAmplificador, eliminarInstrumento, eliminarProveedor, agregarProveedor, amplificador, inicio, instrumento, proveedor, agregarInstrumento, agregarAmplificador

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('proveedor/', proveedor, name="Proveedor"),
    path('instrumento/', instrumento, name="Instrumento"),
    path('amplificador/', amplificador, name="Amplificador"),
    path('agregarproveedor/', agregarProveedor, name="AgregarProveedor"),
    path('agregarinstrumento/', agregarInstrumento, name="AgregarInstrumento"),
    path('agregaramplificador/', agregarAmplificador, name="AgregarAmplificador"),
    path('eliminar-proveedor/<int:id>', eliminarProveedor, name="EliminarProveedor"),
    path('eliminar-instrumento/<int:id>', eliminarInstrumento, name="EliminarInstrumento"),
    path('eliminar-amplificador/<int:id>', eliminarAmplificador, name="EliminarAmplificador"),
    path('editar-proveedor/<int:id>', editarProveedor, name="EditarProveedor"),
    path('editar-instrumento/<int:id>', editarInstrumento, name="EditarInstrumento"),
    path('editar-amplificador/<int:id>', editarAmplificador, name="EditarAmplificador"),
    path('login/', loginView, name="LoginView"),
    path('registro/', register, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="Logout.html"), name="Logout"),
    path('editar-perfil/', editarPerfil, name="EditarPerfil"),
    path('resultado-busqueda-instrumento/', ResultadoBusquedaInstrumento, name="ResultadoBusquedaInstrumento"),
    path('buscarinstrumento/', buscar_instrumento, name="BuscarInstrumento"),
    path('inicio-proveedor/', inicioProveedor, name="InicioProveedor"),
    path('inicio-instrumento/', inicioInstrumento, name="InicioInstrumento"),
    path('inicio-amplificador/', inicioAmplificador, name="InicioAmplificador"),
    path('resultado-busqueda-proveedor/', ResultadoBusquedaProveedor, name="ResultadoBusquedaProveedor"),
    path('buscar-proveedor/', buscar_proveedor, name="BuscarProveedor"),
    path('resultado-busqueda-amplificador/', ResultadoBusquedaAmplificador, name="ResultadoBusquedaAmplificador"),
    path('buscar-amplificador/', buscar_amplificador, name="BuscarAmplificador"),
    path('contacto/', contacto, name="Contacto"),
    path('cambiar-contrasenia/', cambiar_contrasenia, name="CambiarContrasenia"),
]
