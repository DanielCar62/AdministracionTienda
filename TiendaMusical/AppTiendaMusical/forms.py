from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class AgregarProveedor(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    empresa = forms.CharField()
    telefono = forms.IntegerField()
 
class AgregarInstrumento(forms.Form):

    nombre = forms.CharField()
    modelo = forms.IntegerField()
    marca = forms.CharField() 

class AgregarAmplificador(forms.Form):

    modelo = forms.IntegerField()
    marca = forms.CharField() 

class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
    
class Contactar(forms.Form):

	nombre = forms.CharField(max_length = 50)
	apellido = forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)
	mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)

class CambiarContrasenia(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["password1", "password2"]
    
    def clean_password2(self):

        password2=self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas son diferentes")
        return password2

