from django.shortcuts import render,redirect
from .Estructuras.ListaSimple import ListaSimple
from .Estructuras.LecturaArchivo import*
from .Estructuras.ListaPeliculasDC import ListaDobleCircular
from .Estructuras.ListaDoble import ListaDoble
from .Estructuras.ListaCategorias import ListaCategorias
from .Estructuras.ListaPeliculas import ListaDobleCircularPeliculas
from .Estructuras.ListaDobleTarjetas import ListaDobleTarjetas

# Create your views here.
global lista_usuarios
global lista_categorias
global lista_salas
global lista_peliculas
global lista_tarjetas
lista_usuarios=ListaSimple()
lista_categorias=ListaCategorias()
lista_salas=ListaDoble()
lista_peliculas=ListaDobleCircularPeliculas()
lista_tarjetas=ListaDobleTarjetas()
usuario_actual=""

def cargar_xml(request):
    if request.method == 'POST':
        archivo_usuarios='usuarios.xml'
        archivo_categorias='categorias.xml'
        archivo_salas='salas.xml'
        archivo_tarjetas='tarjetas.xml'
        LecturaUsuarios(archivo_usuarios,lista_usuarios)
        LecturaCategorias(archivo_categorias,lista_categorias)
        LectuuraSalas(archivo_salas,lista_salas)
        LecturaPeliculas(archivo_categorias,lista_peliculas)
        LecturaTarjetas(archivo_tarjetas,lista_tarjetas) 
    return render(request, 'usuarios/inicio.html', {'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'filtrados':lista_peliculas,'tarjetas':lista_tarjetas,'categorias':lista_categorias.DevolverAllCategorias()})

def filtrar_img(request):
    if request.method=='POST':
        categoria = request.POST.get('categoria')
        peliculones=lista_peliculas.DevolverObjetoPelicula(categoria)
        return render(request, 'usuarios/inicio.html', {'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'filtrados':peliculones,'tarjetas':lista_tarjetas,'categorias':lista_categorias.DevolverAllCategorias()})
    
    return render(request, 'usuarios/inicio.html', {'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'filtrados':lista_peliculas,'tarjetas':lista_tarjetas,'categorias':lista_categorias.DevolverAllCategorias()})  

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        llave=lista_usuarios.ValidarUsuario(username,password)
        if str(llave).lower()=="administrador":
            usuario_actual=username
            return render(request,'usuarios/menu_admin.html')
        elif str(llave).lower()=="cliente":
            usuario_actual=username
            return render(request,'usuarios/menu_cliente.html')
        else:
            return redirect('login')
    return render(request, 'usuarios/login.html')

def menu_cliente(request):
    return render(request,'usuarios/menu_cliente.html')

def menu_admin(request):
    return render(request,'usuarios/menu_admin.html')




    


