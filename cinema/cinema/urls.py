"""
URL configuration for cinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import cargar_xml,filtrar_img,login,menu_cliente,menu_admin,actualizar_usuario,eliminar_usuario,crear_usuario,crear_pelicula,eliminar_pelicula,actualizar_pelicula,crear_sala,actualizar_sala,eliminar_sala,crear_tarjeta,actualizar_tarjeta,eliminar_tarjeta,volver_admin,volver_login,comprar_boletos,realizar_compra,ver_historial,regresar_menucliente,favoritos,guardar_favoritos,ver_favoritos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', cargar_xml,name='cargar_xml'),
    path('inicio/cargar', filtrar_img,name='filtrar_img'),
    path('login/', login,name='login'),
    path('comprador/', menu_cliente,name='menu_cliente'),
    path('mero/', menu_admin,name='menu_admin'),
    path('mero/actualizar/<str:correo>/', actualizar_usuario, name='actualizar_usuario'),
    path('mero/eliminar/<str:correo>/', eliminar_usuario, name='eliminar_usuario'),
    path('mero/crear/', crear_usuario, name='crear_usuario'),
    path('mero/pelicula/crear/', crear_pelicula, name='crear_pelicula'),
    path('mero/pelicula/eliminar/<str:titulo>/', eliminar_pelicula, name='eliminar_pelicula'),
    path('mero/pelicula/actualizar/<str:titulo>/', actualizar_pelicula, name='actualizar_pelicula'),
    path('mero/sala/crear/', crear_sala, name='crear_sala'),
    path('mero/sala/actualizar/<str:numero>/', actualizar_sala, name='actualizar_sala'),
    path('mero/sala/eliminar/<str:numero>/', eliminar_sala, name='eliminar_sala'),
    path('mero/tarjeta/crear/', crear_tarjeta, name='crear_tarjeta'),
    path('mero/tarjeta/actualizar/<str:titular>/', actualizar_tarjeta, name='actualizar_tarjeta'),
    path('mero/tarjeta/eliminar/<str:titular>/', eliminar_tarjeta, name='eliminar_tarjeta'),
    path('mero/volver/', volver_admin, name='volver_admin'),
    path('mero/regresar/login/', volver_login, name='volver_login'),
    path('clienteu/comprar/',comprar_boletos,name='comprar_boletos'),
    path('clienteu/realizar/',realizar_compra,name='realizar_compra'),
    path('clienteu/historial/',ver_historial,name='ver_historial'),
    path('clienteu/regresarmenu/',regresar_menucliente,name='regresar_menucliente'),
    path('clienteu/favoritos/',favoritos,name='favoritos'),
    path('clienteu/favoritos/guardar/',guardar_favoritos,name='guardar_favoritos'),
    path('clienteu/favoritos/ver/',ver_favoritos,name='ver_favoritos')
]
