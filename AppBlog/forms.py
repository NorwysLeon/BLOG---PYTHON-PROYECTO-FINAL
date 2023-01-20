from django import forms 

class BlogForm(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=100)
    subtitulo=forms.CharField(label="Subtitulo", max_length=100)
    cuerpo=forms.CharField(label="Cuerpo",max_length=500)
    fecha=forms.DateField(label="Fecha")
    autor=forms.CharField(label="Autor", max_length=100)
    imagen=forms.CharField(label="Imagen", max_length=100)