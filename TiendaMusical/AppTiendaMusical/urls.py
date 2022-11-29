from django.urls import path

from .views import editarPerfil, register, loginView, editarAmplificador, editarInstrumento, eliminarAmplificador, eliminarInstrumento, eliminarUsuario, Buscar, agregarUsuario, amplificador, inicio, instrumento, usuario, agregarInstrumento, agregarAmplificador, buscar_instrumento

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('usuario/', usuario, name="Usuario"),
    path('instrumento/', instrumento, name="Instrumento"),
    path('amplificador/', amplificador, name="Amplificador"),
    path('agregarusuario/', agregarUsuario, name="AgregarUsuario"),
    path('agregarinstrumento/', agregarInstrumento, name="AgregarInstrumento"),
    path('agregaramplificador/', agregarAmplificador, name="AgregarAmplificador"),
    path('buscarinstrumento/', buscar_instrumento, name="BuscarInstrumento"),
    path('buscar/', Buscar, name="Buscar"),
    path('eliminar-usuario/<int:id>', eliminarUsuario, name="EliminarUsuario"),
    path('eliminar-instrumento/<int:id>', eliminarInstrumento, name="EliminarInstrumento"),
    path('eliminar-amplificador/<int:id>', eliminarAmplificador, name="EliminarAmplificador"),
    path('editar-instrumento/<int:id>', editarInstrumento, name="EditarInstrumento"),
    path('editar-amplificador/<int:id>', editarAmplificador, name="EditarAmplificador"),
    path('login/', loginView, name="LoginView"),
    path('registro/', register, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="Logout.html"), name="Logout"),
    path('editar-perfil/', editarPerfil, name="EditarPerfil"),
]
