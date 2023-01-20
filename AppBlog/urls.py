from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('blogs/', blogs, name="blogs"),

    path('blogFormulario/', blogFormulario, name="blogFormulario"),
    path('busquedaTitulo/', busquedaTitulo, name="busquedaTitulo"),
    path('buscar/', buscar, name="buscar"),

    path('leerBlogs/', leerBlogs, name="leerBlogs"),    
    

]