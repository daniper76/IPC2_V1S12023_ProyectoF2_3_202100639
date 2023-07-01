from django.shortcuts import render,redirect
from .Estructuras.ListaSimple import ListaSimple
from .Estructuras.LecturaArchivo import*
from .Estructuras.ListaPeliculasDC import ListaDobleCircular
from .Estructuras.ListaDoble import ListaDoble
from .Estructuras.ListaCategorias import ListaCategorias
from .Estructuras.ListaPeliculas import ListaDobleCircularPeliculas
from .Estructuras.ListaDobleTarjetas import ListaDobleTarjetas
from .Estructuras.ListaUsuarioActual import LSUsuario
from .Estructuras.Factura import Factura
import requests

# Create your views here.
global lista_usuarios
global lista_categorias
global lista_salas
global lista_peliculas
global lista_tarjetas
global usuario_actual
global lista_usuario_actual
lista_usuarios=ListaSimple()
lista_categorias=ListaCategorias()
lista_salas=ListaDoble()
lista_peliculas=ListaDobleCircularPeliculas()
lista_tarjetas=ListaDobleTarjetas()
usuario_actual="nada"
lista_usuario_actual=LSUsuario()
lista_usuario_actual.InsertarUsuario("nadie")

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
        response = requests.get('http://localhost:5007/obtenerUsuarios')
        usuarios_API = response.json()
        for usuario_a in usuarios_API['usuario']:
            nuevo_nombre=usuario_a['nombre']
            nuevo_apellido=usuario_a['apellido']
            nuevo_telefono=usuario_a['telefono']
            nuevo_correo=usuario_a['correo']
            nueva_contrasena=usuario_a['contrasena']
            nuevo_rol=usuario_a['rol']
            lista_usuarios.InsertarUsuario(nuevo_nombre,nuevo_apellido,nuevo_telefono,nuevo_correo,nueva_contrasena,nuevo_rol)
        response = requests.get('http://localhost:5007/obtenerPeliculas')
        peliculas_API = response.json()
        for categoria in peliculas_API['categoria']:
            nueva_categoria = categoria['nombre']

            peliculas_a = categoria['peliculas']['pelicula']
            for pelicula_a in peliculas_a:
                nuevo_titulo = pelicula_a['titulo']
                nuevo_director=pelicula_a['director']
                nuevo_anio=pelicula_a['anio']
                nueva_fecha=pelicula_a['fecha']
                nueva_hora=pelicula_a['hora']
                nueva_imagen=pelicula_a['imagen']
                nuevo_precio=pelicula_a['precio']
                lista_peliculas.InsertarPelicula(nuevo_titulo,nuevo_director,nuevo_anio,nueva_fecha,nueva_hora,nueva_categoria,nueva_imagen,nuevo_precio)
        response = requests.get('http://localhost:5007/obtenerSalas')
        salas_API = response.json()
        
        for sala_a in salas_API['cine']['salas']['sala']:
            nuevo_numero=sala_a['numero']
            nuevos_asientos=sala_a['asientos']
            lista_salas.InsertarSala(nuevo_numero,nuevos_asientos)
        response = requests.get('http://localhost:5007/obtenerTarjetas')
        tarjetas_API = response.json()
        for tarjeta_a in tarjetas_API['tarjeta']:
            nuevo_tipo=tarjeta_a['tipo']
            nuevo_numero_tarjeta=tarjeta_a['numero']
            nuevo_titular=tarjeta_a['titular']
            nueva_fecha_vencimiento=tarjeta_a['fecha_expiracion']
            lista_tarjetas.InsertarTarjeta(nuevo_tipo,nuevo_numero_tarjeta,nuevo_titular,nueva_fecha_vencimiento)
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
            lista_usuario_actual.ActualizarUsuario(username)
            return render(request,'usuarios/menu_admin.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})
        elif str(llave).lower()=="cliente":
            usuario_actual=username
            lista_usuario_actual.ActualizarUsuario(username)
            return render(request,'usuarios/menu_cliente.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})
        else:
            return redirect('login')
    return render(request, 'usuarios/login.html')

def menu_cliente(request):
    return render(request,'usuarios/menu_cliente.html')

def menu_admin(request):
    if request.method == 'POST':
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def actualizar_usuario(request,correo):

    usuario=lista_usuarios.DevolverObjetoUsuario(correo)
    if usuario:
        if request.method == 'POST':
            nuevo_correo=request.POST.get('correo')
            nuevo_nombre = request.POST.get('nombre')
            nuevo_apellido = request.POST.get('apellido')
            nuevo_telefono = request.POST.get('telefono')
            nueva_contrasenia=request.POST.get('contrasenia')
            nuevo_rol=request.POST.get('rol')
            lista_usuarios.ModificarNombre(nuevo_correo,nuevo_nombre)
            lista_usuarios.ModificarApellido(nuevo_correo,nuevo_apellido)
            lista_usuarios.ModificarTelefono(nuevo_correo,nuevo_telefono)
            lista_usuarios.ModificarContrasenia(nuevo_correo,nueva_contrasenia)
            lista_usuarios.ModificarRol(nuevo_correo,nuevo_rol)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/actualizar_usuario.html', {'usuario': lista_usuarios.DevolverObjetoUsuario(correo)})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})


def eliminar_usuario(request,correo):

    usuario=lista_usuarios.DevolverObjetoUsuario(correo)
    if usuario:
        lista_usuarios.EliminarUsuario(correo)
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def crear_usuario(request):
    llave=True
    if llave:
        if request.method == 'POST':
            nuevo_correo=request.POST.get('correo')
            nuevo_nombre = request.POST.get('nombre')
            nuevo_apellido = request.POST.get('apellido')
            nuevo_telefono = request.POST.get('telefono')
            nueva_contrasenia=request.POST.get('contrasenia')
            nuevo_rol=request.POST.get('rol')
            lista_usuarios.InsertarUsuario(nuevo_nombre,nuevo_apellido,nuevo_telefono,nuevo_correo,nueva_contrasenia,nuevo_rol)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/crear_usuario.html')
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def crear_pelicula(request):
    llave=True
    if llave:
        if request.method == 'POST':
            nuevo_titulo=request.POST.get('titulo')
            nuevo_director = request.POST.get('director')
            nuevo_anio = request.POST.get('anio')
            nueva_fecha = request.POST.get('fecha')
            nueva_hora=request.POST.get('hora')
            nueva_categoria=request.POST.get('categoria')
            nueva_imagen=request.POST.get('imagen')
            nuevo_precio=request.POST.get('precio')
            lista_peliculas.InsertarPelicula(nuevo_titulo,nuevo_director,nuevo_anio,nueva_fecha,nueva_hora,nueva_categoria,nueva_imagen,nuevo_precio)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/crear_pelicula.html')
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def eliminar_pelicula(request,titulo):
    pelicula=lista_peliculas.DevolverObjetoPeliculaWeb(titulo)
    if pelicula:
        lista_peliculas.EliminarPelicula(titulo)
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def actualizar_pelicula(request,titulo):
    pelicula=lista_peliculas.DevolverObjetoPeliculaWeb(titulo)
    if pelicula:
        if request.method == 'POST':
            nuevo_titulo=request.POST.get('titulo')
            nuevo_director = request.POST.get('director')
            nuevo_anio = request.POST.get('anio')
            nueva_fecha = request.POST.get('fecha')
            nueva_hora=request.POST.get('hora')
            nueva_categoria=request.POST.get('categoria')
            nueva_imagen=request.POST.get('imagen')
            nuevo_precio=request.POST.get('precio')
            lista_peliculas.ModificarDirector(nuevo_titulo,nuevo_director)
            lista_peliculas.ModificarAnio(nuevo_titulo,nuevo_anio)
            lista_peliculas.ModificarFecha(nuevo_titulo,nueva_fecha)
            lista_peliculas.ModificarHora(nuevo_titulo,nueva_hora)
            lista_peliculas.ModificarCategoria(nuevo_titulo,nueva_categoria)
            lista_peliculas.ModificarImagen(nuevo_titulo,nueva_imagen)
            lista_peliculas.ModificarPrecio(nuevo_titulo,nuevo_precio)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/actualizar_pelicula.html', {'pelicula': lista_peliculas.DevolverObjetoPeliculaWeb(titulo)})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def crear_sala(request):
    llave=True
    if llave:
        if request.method == 'POST':
            nuevo_numero=request.POST.get('numero')
            nuevos_asientos = request.POST.get('asientos')
            lista_salas.InsertarSala(nuevo_numero,nuevos_asientos)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/crear_sala.html')
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def actualizar_sala(request,numero):
    sala=lista_salas.DevolverObjetoSalaWeb(numero)
    if sala:
        if request.method == 'POST':
            nuevo_numero=request.POST.get('numero')
            nuevos_asientos = request.POST.get('asientos')
            lista_salas.ModificarAsientos(nuevo_numero,nuevos_asientos)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/actualizar_sala.html', {'sala': lista_salas.DevolverObjetoSalaWeb(numero)})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def eliminar_sala(request,numero):
    sala=lista_salas.DevolverObjetoSalaWeb(numero)
    if sala:
        lista_salas.eliminar(numero)
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def crear_tarjeta(request):
    llave=True
    if llave:
        if request.method == 'POST':
            nuevo_tipo=request.POST.get('tipo')
            nuevo_numero = request.POST.get('numero')
            nuevo_titular = request.POST.get('titular')
            nueva_fecha = request.POST.get('fecha')
            lista_tarjetas.InsertarTarjeta(nuevo_tipo,nuevo_numero,nuevo_titular,nueva_fecha)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/crear_tarjeta.html')
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def actualizar_tarjeta(request,titular):
    tarjeta=lista_tarjetas.DevolverObjetoTarjetaWeb(titular)
    if tarjeta:
        if request.method == 'POST':
            nuevo_tipo=request.POST.get('tipo')
            nuevo_numero = request.POST.get('numero')
            nuevo_titular = request.POST.get('titular')
            nueva_fecha = request.POST.get('fecha')
            lista_tarjetas.ModificarTipo(nuevo_titular,nuevo_tipo)
            lista_tarjetas.ModificarNumero(nuevo_titular,nuevo_numero)
            lista_tarjetas.ModificarFecha(nuevo_titular,nueva_fecha)
            return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
        return render(request, 'usuarios/actualizar_tarjeta.html', {'tarjeta': lista_tarjetas.DevolverObjetoTarjetaWeb(titular)})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def eliminar_tarjeta(request,titular):
    tarjeta=lista_tarjetas.DevolverObjetoTarjetaWeb(titular)
    if tarjeta:
        lista_tarjetas.eliminar(titular)
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
    return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})

def volver_admin(request):
    if request.method == 'POST':
        return render(request,'usuarios/menu_admin.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})

def volver_login(request):
    return render(request, 'usuarios/login.html')


def comprar_boletos(request):
    if request.method == 'POST':
        tipo_pagos=['credito','debito','efectivo']
        return render(request, 'usuarios/comprar_boletos.html', {'peliculas':lista_peliculas,'salas':lista_salas,'pagos':tipo_pagos})

    
def realizar_compra(request):
    if request.method == 'POST':
        nombre_factura = request.POST.get('nombre')
        nit_factura = request.POST.get('nit')
        direccion_factura=request.POST.get('direccion')
        cantidad_boletos=request.POST.get('cantidad')
        asientos_factura=request.POST.get('asientos')
        pelicula_seleccionada = request.POST.get('pelicula')
        sala_seleccionada = request.POST.get('sala')
        pago_seleccionado = request.POST.get('pago')
        monto_factura=int(cantidad_boletos)*int(lista_peliculas.DevolverPrecioPelicula(pelicula_seleccionada))
        nueva_factura=Factura(nombre_factura,direccion_factura,nit_factura,str(monto_factura),cantidad_boletos,asientos_factura,sala_seleccionada,pelicula_seleccionada,pago_seleccionado)
        lista_usuarios.GuardarFactura(lista_usuario_actual.DevolverUsuarioActual(),nueva_factura)
        return render(request,'usuarios/menu_cliente.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})

def ver_historial(request):
    if request.method == 'POST':
        return render(request,'usuarios/historial.html',{'facturas':lista_usuarios.DevolverHistorialUsuario(lista_usuario_actual.DevolverUsuarioActual())})
    
def regresar_menucliente(request):
    if request.method == 'POST':
        return render(request,'usuarios/menu_cliente.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})
    
def favoritos(request):
    if request.method == 'POST':
        return render(request,'usuarios/favoritos.html',{'peliculas':lista_peliculas})

def guardar_favoritos(request):
    if request.method == 'POST':
        pelicula_seleccionada = request.POST.get('pelicula')
        lista_usuarios.AgregarPeliculaFavorita(lista_usuario_actual.DevolverUsuarioActual(),lista_peliculas.DevolverObjetoPeliculaWeb(pelicula_seleccionada))
        return render(request,'usuarios/menu_cliente.html',{'usuario_actual':lista_usuario_actual.DevolverUsuarioActual()})

def ver_favoritos(request):
    if request.method == 'POST':
        return render(request,'usuarios/ver_favoritos.html',{'favoritos':lista_usuarios.DevolverFavoritoslUsuario(lista_usuario_actual.DevolverUsuarioActual())})

def actualizar_xml(request):
    if request.method=='POST':
        lista_usuarios.escribirXML()
        lista_tarjetas.escribirXML()
        lista_salas.escribirXML()
        lista_peliculas.EscribirXML()
        return render(request,'usuarios/gestionar_cine.html',{'usuarios': lista_usuarios,'salas':lista_salas,'peliculas':lista_peliculas,'tarjetas':lista_tarjetas})
