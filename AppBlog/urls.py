from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="inicio"),
    path('acercademi/', acercademi, name="acercademi"),
    path('blogs/', blogs, name="blogs"),

    path('blogFormulario/', blogFormulario, name="blogFormulario"),
    path('busquedaTitulo/', busquedaTitulo, name="busquedaTitulo"),
    path('buscar/', buscar, name="buscar"),

    path('leerBlogs/', leerBlogs, name="leerBlogs"),    
    path('eliminarBlog/<id>', eliminarBlog, name="eliminarBlog"),
    path('editarBlog/<id>', editarBlog, name="editarBlog"),

    path('blog/list/', BlogList.as_view(), name="blog_list"),
    path('blog/<pk>', BlogDetalle.as_view(), name="blog_detalle"),

    path('register/', register, name="register"),
    path('login/', login_usuario, name="login"), #No se puede llamar solo login porque ya existe una funcion login por eso login_request, puede tener cualquier nombre.
    path('logout/', LogoutView.as_view() , name="logout"),
    
]