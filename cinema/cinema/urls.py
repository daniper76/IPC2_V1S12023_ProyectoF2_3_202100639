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
from usuarios.views import cargar_xml,filtrar_img,login,menu_cliente,menu_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', cargar_xml,name='cargar_xml'),
    path('inicio/cargar', filtrar_img,name='filtrar_img'),
    path('login/', login,name='login'),
    path('cliente/', menu_cliente,name='menu_cliente'),
    path('admin/', menu_admin,name='menu_admin')
]
