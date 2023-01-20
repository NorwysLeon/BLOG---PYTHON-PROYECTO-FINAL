from django.db import models

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