from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=100)
    subtitulo=forms.CharField(label="Subtitulo", max_length=100)
    cuerpo=forms.CharField(label="Cuerpo",max_length=500)
    fecha=forms.DateField(label="Fecha")
    autor=forms.CharField(label="Autor", max_length=100)
    imagen=forms.CharField(label="Titulo", max_length=100)

    

class RegistroUsuarioForm(UserCreationForm): #Estos son los campos del admin usuario, username esta por deecto
    email= forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
  
    class Meta: #configura el formulario
        model=User
        fields= ["username", "email", "password1", "password2"] #Camposque muestra el formulario
        help_texts= {k:"" for k in fields} #Asigna un valor vacio a cada texto de ayuda del formulario.


class UserEditForm(UserCreationForm): 
    email= forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")
  
    class Meta: #configura el formulario
        model=User
        fields= ["email", "password1", "password2", "first_name", "last_name"] #Camposque muestra el formulario
        help_texts= {k:"" for k in fields} #Asigna un valor vacio a cada texto de ayuda del formulario.


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class PerfilForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    nombre=forms.CharField(label="nombre")
    descripcion=forms.CharField(label="descripcion")
    web=forms.URLField(label="web")
    email=forms.EmailField(label="email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    
    
