from .Peli import Pelicula
class ListaDobleCircularPeliculas:

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def InsertarPelicula(self,titulo,director,anio,fecha,hora,categoria,imagen,precio):
        nueva_pelicula=Pelicula(titulo,director,anio,fecha,hora,categoria,imagen,precio)

        if self.primero is None:
            nueva_pelicula.siguiente=nueva_pelicula
            nueva_pelicula.anterior=nueva_pelicula
            self.primero=nueva_pelicula
            self.ultimo=nueva_pelicula

        else:
            nueva_pelicula.anterior=self.ultimo
            self.ultimo.siguiente=nueva_pelicula
            nueva_pelicula.siguiente=self.primero
            self.primero.anterior=nueva_pelicula
            self.ultimo=nueva_pelicula
        
    def MostrarPeliculas(self):
        aux=self.primero

        while True:
            print("------------------------------------------------------")
            print("\tTítulo de la Pelicula: "+aux.ObtenerTitulo())
            print("\t\tPelicula dirigida por: "+aux.ObtenerDirector())
            print("\t\tEl año del estreno de la Película es: "+aux.ObtenerAnio())
            print("\t\tFecha de la Función: "+aux.ObtenerFecha())
            print("\t\tHora de la Función"+aux.ObtenerHora())
            print("\t\tCategoría de la Función"+aux.ObtenerCategoria())
            print("-------------------------------------------------------------")
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def NuevaPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return False
            aux=aux.siguiente
            if aux==self.primero:
                return True
        return True

    
    def EliminarPelicula(self,titulo):
        if self.primero is None:
             print("la lista esta vacia")
        else:
            aux = self.primero
            while aux is not None:
                if aux.ObtenerTitulo() == titulo:
                    if aux == self.primero:
                        self.ultimo.siguiente=aux.siguiente
                        aux.siguiente.anterior=self.ultimo
                        self.primero=aux.siguiente
                        aux.anterior=None
                        aux.siguiente=None
                    elif aux == self.ultimo:
                        aux.anterior.siguiente=self.primero
                        self.primero.anterior=aux.anterior
                        self.ultimo=aux.anterior
                        aux.siguiente=None
                        aux.anterior=None
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                        aux.siguiente=None
                        aux.anterior=None
                    return
                aux = aux.siguiente
                if aux==self.primero:
                    break
            

    def ModificarDirector(self,titulo,director):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.director=director
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarAnio(self,titulo,anio):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.anio=anio
            aux=aux.siguiente
            if aux==self.primero:
                break


    def ModificarFecha(self,titulo,fecha):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.fecha=fecha
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarHora(self,titulo,hora):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.hora=hora
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarCategoria(self,titulo,categoria):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.categoria=categoria
            aux=aux.siguiente
            if aux==self.primero:
                break
    def ModificarImagen(self,titulo,imagen):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.imagen=imagen
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarPrecio(self,titulo,precio):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.precio=precio
            aux=aux.siguiente
            if aux==self.primero:
                break

    
    def MostrarDetallePelicula(self,titulo):
        aux=self.primero

        while True:
            if aux.ObtenerTitulo()==titulo:
                print("\tTítulo de la Pelicula: "+aux.ObtenerTitulo())
                print("\tPelicula dirigida por: "+aux.ObtenerDirector())
                print("\tEl año del estreno de la Película es: "+aux.ObtenerAnio())
                print("\tFecha de la Función: "+aux.ObtenerFecha())
                print("\tHora de la Función"+aux.ObtenerHora())
                print("\tCategoria de la Función"+aux.ObtenerCategoria())
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def MostrarCartelera(self):
        aux=self.primero

        while True:
            print("\t***"+aux.ObtenerTitulo())
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def DevolverPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return aux
            aux=aux.siguiente
            if aux==self.primero:
                return None
        
    
    def ExistePeli(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return True
            aux=aux.siguiente
            if aux==self.primero:
                return None

    def EscribirXML(self):
        aux=self.primero
        archivo = open("categorias.xml", "w")
        archivo.write("<categorias>\n")
        while True:
            archivo.write("\t<categoria>\n")
            categoria_actual=aux.ObtenerCategoria()
            archivo.write("\t\t<nombre>"+str(aux.ObtenerCategoria())+"</nombre>\n")
            archivo.write("\t\t<peliculas>\n")
            while True:
                archivo.write("\t\t\t<pelicula>\n")
                archivo.write("\t\t\t\t<titulo>"+str(aux.ObtenerTitulo())+"</titulo>\n")
                archivo.write("\t\t\t\t<director>"+str(aux.ObtenerDirector())+"</director>\n")
                archivo.write("\t\t\t\t<anio>"+str(aux.ObtenerAnio())+"</anio>\n")
                archivo.write("\t\t\t\t<fecha>"+str(aux.ObtenerFecha())+"</fecha>\n")
                archivo.write("\t\t\t\t<hora>"+str(aux.ObtenerHora())+"</hora>\n")
                archivo.write("\t\t\t\t<imagen>"+str(aux.ObtenerImagen())+"</imagen>\n")
                archivo.write("\t\t\t\t<precio>"+str(aux.ObtenerPrecio())+"</precio>\n")
                archivo.write("\t\t\t</pelicula>\n")
                aux=aux.siguiente
                if aux.ObtenerCategoria()!=categoria_actual:
                    archivo.write("\t\t</peliculas>\n")
                    archivo.write("\t</categoria>\n")
                    break
            if aux==self.primero:
                archivo.write("</categorias>\n")
                break
        archivo.close()                 

    def loop(self):
        aux = self.primero
        while aux:
            yield aux
            aux=aux.siguiente
            if aux==self.primero:
                break


    def __iter__(self):
        return iter(self.loop())


    def DevolverObjetoPelicula(self,categoria):
        lista=[]
        if self.primero==None:
            print("vacio")
        else:
            aux=self.primero
            while True:
                if aux.ObtenerCategoria()==categoria:
                    lista.append(aux)
                aux=aux.siguiente
                if aux==self.primero:
                    break
        return lista
    
    def DevolverObjetoPeliculaWeb(self,titulo):
        aux=self.primero
        while True:
            if aux.ObtenerTitulo()==titulo:
                return aux
            aux=aux.siguiente
            if aux==self.primero:
                break

    def DevolverPrecioPelicula(self,titulo):
        aux=self.primero
        while True:
            if aux.ObtenerTitulo()==titulo:
                return aux.ObtenerPrecio()
            aux=aux.siguiente
            if aux==self.primero:
                break

            

            



