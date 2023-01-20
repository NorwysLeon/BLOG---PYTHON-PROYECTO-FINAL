from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

from AppBlog.forms import BlogForm

from django.views.generic import ListView, DetailView

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

def acercademi(request):
    return render(request, "acercademi.html")

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
            blogs=Blog.objects.all()
            return render(request, "leerBlogs.html", {"blogs":blogs, "mensaje": "Post guardado correctamente"})       
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

def eliminarBlog(request, id):
    blog= Blog.objects.get(id=id) #Trae los datos del model Blog que concuerda con el id. como es get es uno solo.
    blog.delete()
    blogs=Blog.objects.all()
    return render(request, "leerBlogs.html", {"blogs":blogs, "mensaje": "Blog eliminado correctamente"})


def editarBlog(request, id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        form= BlogForm(request.POST)
        if form.is_valid():         #Verifica si el formulario es valido
            info=form.cleaned_data  #transforma del formulario al diccionario
            blog.titulo=info["titulo"]
            blog.subtitulo=info["subtitulo"]
            blog.cuerpo=info["cuerpo"]
            blog.fecha=info["fecha"]
            blog.autor=info["autor"]
            blog.imagen=info["imagen"]
            blog.save()
            blogs=Blog.objects.all()
            return render (request, "leerBlogs.html", {"blogs": blogs, "mensaje": "Blog editado correctamente!"})
            pass
    else:
        formulario= BlogForm(initial={"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "fecha":blog.fecha, "autor":blog.autor, "imagen":blog.imagen})  #Trae los datos iniciales del Blog
        return render (request, "editarBlog.html", {"form": formulario})

#Permite listar todos los blogs de la BD, con información mínima de dicho blog.
class BlogList(ListView):
    model=Blog
    template_name= "BlogList.html"

#Al clickear en "Leer más" navega al detalle de cada blog mediante un 'blog/<pk>'.
class BlogDetalle(DetailView):
    model=Blog
    template_name="BlogDetalle.html"