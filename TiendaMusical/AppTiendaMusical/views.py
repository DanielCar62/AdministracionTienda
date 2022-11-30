from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Usuario, Instrumento, Amplificador
from .forms import AgregarUsuario, AgregarInstrumento, AgregarAmplificador, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    
    return render(request, "Inicio.html")

@login_required
def usuario(request):

    lista = Usuario.objects.all()
    return render(request, "Usuarios.html", {"usuarios": lista})

@login_required
def instrumento(request):

    lista_instrumentos = Instrumento.objects.all()
    return render(request, "Instrumento.html", {"instrumentos": lista_instrumentos})

@login_required
def amplificador(request):

    lista_amplificadores = Amplificador.objects.all()
    return render(request, "Amplificador.html", {"amplificadores":lista_amplificadores})

def agregarUsuario(request):

    if request.method == "POST":
        formulario_usuario = AgregarUsuario(request.POST)
        if formulario_usuario.is_valid():
            data = formulario_usuario.cleaned_data
            usuario = Usuario(nombre=data["nombre"], Apellido=data["apellido"], email=data["email"])
            usuario.save()
            return redirect("Usuario")
    else:
        formulario_usuario = AgregarUsuario()

    return render(request, "AgregarUsuario.html", {"formulario_usuario" : formulario_usuario})

def agregarInstrumento(request):
    
    if request.method == "POST":
        formulario_instrumento = AgregarInstrumento(request.POST)
        if formulario_instrumento.is_valid():
            data = formulario_instrumento.cleaned_data
            instrumento = Instrumento(nombre=data["nombre"],modelo=data["modelo"],marca=data["marca"])
            instrumento.save()
            return redirect("Instrumento")
    else:
        formulario_instrumento = AgregarInstrumento()
    return render(request, "AgregarInstrumento.html", {"formulario_instrumento": formulario_instrumento})

def agregarAmplificador(request):

    if request.method == "POST":
        formulario_amplificador = AgregarAmplificador(request.POST)
        if formulario_amplificador.is_valid():
            data = formulario_amplificador.cleaned_data
            amplificador = Amplificador(modelo=data["modelo"],marca=data["marca"])
            amplificador.save()
            return redirect("Amplificador")
    else:
        formulario_amplificador = AgregarAmplificador()
    return render(request, "AgregarAmplificador.html", {"formulario_amplificador":formulario_amplificador})

@login_required
def buscar_instrumento(request):
    return render(request, "BuscarInstrumento.html")

def Buscar(request):
    
    modelo_buscado = request.GET["modelo"]
    instrumento = Instrumento.objects.get(modelo = modelo_buscado)
    return render(request, "ResultadoBusqueda.html", {"instrumento":instrumento, "modelo":modelo_buscado})

def eliminarUsuario(request, id):

    if request.method == "POST":
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        
        lista = Usuario.objects.all()
        return render(request, "Usuarios.html", {"usuarios": lista})

def eliminarInstrumento(request, id):

    if request.method =="POST":
        instrumento = Instrumento.objects.get(id=id)
        instrumento.delete()

        lista_instrumentos = Instrumento.objects.all()
        return render(request, "Instrumento.html", {"instrumentos": lista_instrumentos})

def eliminarAmplificador(request, id):

    if request.method == "POST":
        amplificador = Amplificador.objects.get(id=id)
        amplificador.delete()

        lista_amplificadores = Amplificador.objects.all()
        return render(request, "Amplificador.html", {"amplificadores":lista_amplificadores})

def editarInstrumento(request, id):

    instrumento = Instrumento.objects.get(id=id)
    if request.method == "POST":
        formulario_instrumento = AgregarInstrumento(request.POST)
        if formulario_instrumento.is_valid():
            data = formulario_instrumento.cleaned_data
            instrumento.nombre = data["nombre"]
            instrumento.modelo = data["modelo"]
            instrumento.marca = data["marca"]
            instrumento.save()

            lista_instrumentos = Instrumento.objects.all()
            return render(request, "Instrumento.html", {"instrumentos": lista_instrumentos})
    
    else:
        formulario_instrumento = AgregarInstrumento(initial= {
            "nombre": instrumento.nombre,
            "modelo": instrumento.modelo,
            "marca": instrumento.marca,
        })
        return render(request, "EditarInstrumento.html", {"formulario_instrumento": formulario_instrumento, "id": instrumento.id})

def editarAmplificador(request, id):

    amplificador = Amplificador.objects.get(id=id)
    if request.method == "POST":
        formulario_amplificador = AgregarAmplificador(request.POST)
        if formulario_amplificador.is_valid():
            data = formulario_amplificador.cleaned_data
            amplificador.modelo = data["modelo"]
            amplificador.marca = data["marca"]
            amplificador.save()

            lista_amplificadores = Amplificador.objects.all()
            return render(request, "Amplificador.html", {"amplificadores": lista_amplificadores})
    
    else:
        formulario_amplificador= AgregarAmplificador(initial= {
            "modelo": amplificador.modelo,
            "marca": amplificador.marca,
        })
        return render(request, "EditarAmplificador.html", {"formulario_amplificador": formulario_amplificador, "id": amplificador.id})

def loginView(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data["username"]
            contrasenia = data["password"]
            user =authenticate(username=usuario, password=contrasenia)
            
            if user:
                login(request, user)
                return render(request, "Inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            else:
                return render(request, "Inicio.html", {"mensaje": f'Datos incorrectos'})
        
        else:
            return render(request, "Inicio.html", {"mensaje": f'Formulario invalido'})

    else:
        formulario = AuthenticationForm()
        return render(request, "Login.html", {"formulario": formulario})

def register(request):
    
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data["username"]
            formulario.save()
            return render(request, "Inicio.html", {"mensaje": f'Usuario {usuario} creado'})
        else:
            return render(request, "Inicio.html", {"mensaje": f'No se logro crear el usuario'})

    else:
        formulario = UserCreationForm()
        return render(request, "Registro.html", {"formulario":formulario})

def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(request, "Inicio.html", {"mensaje": f'Los datos se han actualizado'})
        return render(request, "Inicio.html", {"mensaje": "Contraseñas no coinciden"}) 
    else:
        formulario = UserEditForm(instance=request.user)
        return render(request, "EditarPerfil.html", {"formulario":formulario})

