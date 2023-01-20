from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

from AppBlog.forms import BlogForm
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

#Este se usa cuando se realiza el formulario en el html
"""def blogFormulario(request):
    if request.method=="POST":
        titulo=request.POST["titulo"]
        subtitulo=request.POST["subtitulo"]
        cuerpo=request.POST["cuerpo"]
        fecha=request.POST["fecha"]
        autor=request.POST["autor"]
        imagen=request.POST["imagen"]
        blog=Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, fecha=fecha, autor=autor, imagen=imagen)
        blog.save()
        return render(request, "inicio.html", {"mensaje": "Post creado correctamente"})
    else:
        return render(request, "blogFormulario.html")"""


def blogFormulario(request):
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            fecha= informacion["fecha"]
            autor= informacion["autor"]
            imagen= informacion["imagen"]
            blog= Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, fecha=fecha, autor=autor, imagen=imagen)
            blog.save()
            return render(request, "inicio.html", {"mensaje": "Post guardado correctamente"})       
    else:
        formulario=BlogForm()
        return render(request, "blogFormulario.html", {"form": formulario, "mensaje": "Información no valida"})


def busquedaTitulo(requets):
    return render(requets, "busquedaTitulo.html")

def buscar(request):
    titulo=request.GET["titulo"]
    if titulo!="":
        blogs=Blog.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosBusqueda.html", {"blogs":blogs})
    else:
        return render (request, "busquedaTitulo.html", {"mensaje": "Favor ingresar un titulo para buscar"})


def leerBlogs(request):
    blogs=Blog.objects.all()
    return render (request, "leerBlogs.html", {"blogs":blogs})
    