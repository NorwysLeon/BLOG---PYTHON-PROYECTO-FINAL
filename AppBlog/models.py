from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.CharField(max_length=500)
    fecha=models.DateField()
    autor=models.CharField(max_length=100)
    imagen=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} - {self.cuerpo} - {self.fecha} - {self.autor} {self.imagen}"

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
class Perfil(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    nombre=models.CharField(max_length=100)
    web=models.URLField()
    email=models.EmailField()
    descripcion=models.CharField(max_length=200)
    password1=models.CharField(max_length=8)
    password2=models.CharField(max_length=8)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.imagen} - {self.nombre} - {self.descripcion} - {self.web} - {self.email}"