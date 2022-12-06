from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Instrumento, Amplificador, Proveedor
from .forms import AgregarProveedor, AgregarInstrumento, AgregarAmplificador, UserEditForm, Contactar, CambiarContrasenia
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def inicio(request):
    
    return render(request, "Inicio.html", {"mensaje": f'Inicie sesion para acceder al administrador'})

def about(request):
    
    return render(request, "About.html")

@login_required
def inicioProveedor(request):
    
    return render(request, "InicioProveedor.html")

@login_required
def inicioInstrumento(request):
    
    return render(request, "InicioInstrumento.html")

@login_required
def inicioAmplificador(request):
    
    return render(request, "InicioAmplificador.html")

@login_required
def proveedor(request):

    lista = Proveedor.objects.all()
    return render(request, "Proveedores.html", {"proveedores": lista})

@login_required
def instrumento(request):

    lista_instrumentos = Instrumento.objects.all()
    return render(request, "Instrumento.html", {"instrumentos": lista_instrumentos})

@login_required
def amplificador(request):

    lista_amplificadores = Amplificador.objects.all()
    return render(request, "Amplificador.html", {"amplificadores":lista_amplificadores})

@login_required
def agregarProveedor(request):

    if request.method == "POST":
        formulario_proveedor = AgregarProveedor(request.POST)
        if formulario_proveedor.is_valid():
            data = formulario_proveedor.cleaned_data
            proveedor = Proveedor(nombre=data["nombre"], Apellido=data["apellido"], email=data["email"], empresa=data["empresa"], telefono=data["telefono"])
            proveedor.save()
            return redirect("Proveedor")
    else:
        formulario_proveedor = AgregarProveedor()

    return render(request, "AgregarProveedor.html", {"formulario_proveedor" : formulario_proveedor})

@login_required
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

@login_required
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
def eliminarProveedor(request, id):

    if request.method == "POST":
        proveedor = Proveedor.objects.get(id=id)
        proveedor.delete()
        
        lista = Proveedor.objects.all()
        return render(request, "Proveedores.html", {"proveedores": lista})

@login_required
def eliminarInstrumento(request, id):

    if request.method =="POST":
        instrumento = Instrumento.objects.get(id=id)
        instrumento.delete()

        lista_instrumentos = Instrumento.objects.all()
        return render(request, "Instrumento.html", {"instrumentos": lista_instrumentos})

@login_required
def eliminarAmplificador(request, id):

    if request.method == "POST":
        amplificador = Amplificador.objects.get(id=id)
        amplificador.delete()

        lista_amplificadores = Amplificador.objects.all()
        return render(request, "Amplificador.html", {"amplificadores":lista_amplificadores})

@login_required
def editarProveedor(request, id):

    proveedor = Proveedor.objects.get(id=id)
    if request.method == "POST":
        formulario_proveedor = AgregarProveedor(request.POST)
        if formulario_proveedor.is_valid():
            data = formulario_proveedor.cleaned_data
            proveedor.nombre = data["nombre"]
            proveedor.Apellido = data["apellido"]
            proveedor.email = data["email"]
            proveedor.empresa = data["empresa"]
            proveedor.telefono = data["telefono"]
            proveedor.save()

            lista_proveedores = Proveedor.objects.all()
            return render(request, "Proveedores.html", {"proveedores": lista_proveedores})
    
    else:
        formulario_proveedor = AgregarProveedor(initial= {
            "nombre": proveedor.nombre,
            "apellido": proveedor.Apellido,
            "email": proveedor.email,
            "empresa": proveedor.empresa,
            "telefono": proveedor.telefono,
        })
        return render(request, "EditarProveedor.html", {"formulario_proveedor": formulario_proveedor, "id": proveedor.id})

@login_required
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

@login_required
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

@login_required
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

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.save()
            return render(request, "Inicio.html", {"mensaje": f'Los datos se han actualizado'}) 
    else:
        formulario = UserEditForm(instance=request.user)
        return render(request, "EditarPerfil.html", {"formulario":formulario})

@login_required
def buscar_instrumento(request):
    return render(request, "BuscarInstrumento.html")

@login_required
def ResultadoBusquedaInstrumento(request):
    
    modelo_buscado = request.GET["modelo"]
    if Instrumento.objects.filter(modelo=modelo_buscado).exists():
        instrumento = Instrumento.objects.get(modelo = modelo_buscado)
        return render(request, "ResultadoBusquedaInstrumento.html", {"instrumento":instrumento, "modelo":modelo_buscado})
    else:
        return render(request, "Inicio.html", {"mensaje": "No hay coincidencias"})

@login_required
def buscar_proveedor(request):
    return render(request, "BuscarProveedor.html")

@login_required
def ResultadoBusquedaProveedor(request):
    
    nombre_buscado = request.GET["nombre"]
    if Proveedor.objects.filter(nombre=nombre_buscado).exists():
        proveedor = Proveedor.objects.get(nombre = nombre_buscado)
        return render(request, "ResultadoBusquedaProveedor.html", {"proveedor":proveedor, "nombre":nombre_buscado})
    else:
        return render(request, "Inicio.html", {"mensaje": "No hay coincidencias"})

@login_required
def buscar_amplificador(request):
    return render(request, "BuscarAmplificador.html")

@login_required
def ResultadoBusquedaAmplificador(request):
    
    modelo_buscado = request.GET["modelo"]
    if Amplificador.objects.filter(modelo=modelo_buscado).exists():
        amplificador = Amplificador.objects.get(modelo = modelo_buscado)
        return render(request, "ResultadoBusquedaAmplificador.html", {"amplificador":amplificador, "modelo":modelo_buscado})
    else:
        return render(request, "Inicio.html", {"mensaje": "No hay coincidencias"})

@login_required
def contacto(request):
	if request.method == 'POST':
		formulario = Contactar(request.POST)
		if formulario.is_valid():
			titulo = "Consulta del sitio web" 
			cuerpo = {
			'nombre': formulario.cleaned_data['nombre'], 
			'apellido': formulario.cleaned_data['apellido'], 
			'email': formulario.cleaned_data['email'], 
			'mensaje':formulario.cleaned_data['mensaje'], 
			}
			mensaje = "\n".join(cuerpo.values())

			try:
				send_mail(titulo, mensaje, 'admin@gmail.com', ['admin@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("Contacto")
      
	formulario = Contactar()
	return render(request, "Contacto.html", {'formulario':formulario})

@login_required
def cambiar_contrasenia(request):
    usuario = request.user
    if request.method == "POST":
        formulario = CambiarContrasenia(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.set_password(data["password1"])
            usuario.save()
            return render(request, "Logout.html", {"mensaje": f'Los datos se han actualizado'})
        return render(request, "Inicio.html", {"mensaje": "Contraseñas no coinciden"}) 
    else:
        formulario = CambiarContrasenia(instance=request.user)
        return render(request, "CambiarContrasenia.html", {"formulario":formulario})