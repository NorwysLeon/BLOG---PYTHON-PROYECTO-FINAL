from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
# Create your views here.



def blog(request):
    blogues= Blog(titulo= "Python", subtitulo="Lenguaje", cuerpo="xxxxxx", fecha="2023-01-20", autor="", imagen="")
    blogues.save()
    cadena_texto=f"Blog guardado"
    return HttpResponse(cadena_texto)

def blogs(request):
    return render(request, "blogs.html")

def inicio(request):
    return render(request, "inicio.html")