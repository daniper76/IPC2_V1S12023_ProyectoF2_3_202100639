from .Tarjeta import Tarjeta

class ListaDobleTarjetas:

    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def InsertarTarjeta(self,tipo,numero,titular,fecha):
        nueva_tarjeta=Tarjeta(tipo,numero,titular,fecha)
        if self.primero is None:
            self.primero = nueva_tarjeta
            self.ultimo = nueva_tarjeta
        else:
            nueva_tarjeta.anterior = self.ultimo
            self.ultimo.siguiente = nueva_tarjeta
            self.ultimo = nueva_tarjeta
    
    def MostrarTarjeta(self):
        aux=self.primero
        print("********Salas de Cine:*********\n")
        while aux is not None:
            print("Tipo de Tarjeta: "+str(aux.ObtenerTipo()))
            print("\tNúmero de Tarjeta: "+str(aux.ObtenerNumero())+"\n")
            print("\tTitular de Tarjeta: "+str(aux.ObtenerTitular())+"\n")
            print("\tFecha de Caducidad de Tarjeta: "+str(aux.ObtenerFecha())+"\n")
            aux=aux.siguiente

    def loop(self):
        aux=self.primero
        while aux:
            yield aux
            aux = aux.siguiente

    def __iter__(self):
        return iter(self.loop())

    def eliminar(self,titular):
        if self.primero is None:
            print("la lista esta vacia")
        else:
            aux = self.primero
            while aux is not None:
                if aux.ObtenerTitular()==titular:
                    if aux == self.primero:
                        self.primero = self.primero.siguiente
                        self.primero.anterior = None
                    elif aux == self.ultimo:
                        self.ultimo = self.ultimo.anterior
                        self.ultimo.siguiente = None
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                    print("ELIMINADO")
                    return
                aux = aux.siguiente
            print("Tarjeta No Encontrada")
    
    def ModificarTitular(self,titular,nuevo_titular):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                aux.titular=nuevo_titular
            aux=aux.siguiente
    
    def ModificarFecha(self,titular,nueva_fecha):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                aux.fecha=nueva_fecha
            aux=aux.siguiente

    def ModificarTipo(self,titular,nuevo_tipo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                aux.tipo=nuevo_tipo
            aux=aux.siguiente

    def ModificarNumero(self,titular,nuevo_numero):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                aux.numero=nuevo_numero
            aux=aux.siguiente

    def MostrarDetalleTarjeta(self,titular):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                print("Tipo de Tarjeta: "+str(aux.ObtenerTipo()))
                print("\tNúmero de Tarjeta: "+str(aux.ObtenerNumero())+"\n")
                print("\tTitular de Tarjeta: "+str(aux.ObtenerTitular())+"\n")
                print("\tFecha de Caducidad de Tarjeta: "+str(aux.ObtenerFecha())+"\n")
                break
            aux=aux.siguiente
    
    def ExisteTarjeta(self,numero):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNumero()==numero:
                return True
            aux=aux.siguiente
        return False
    
    def escribirXML(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("tarjetas.xml", "w")
            archivo.write("<tarjetas>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t<tarjeta>\n")
                archivo.write("\t\t<tipo>" + str(aux.ObtenerTipo()) + "</tipo>\n")
                archivo.write("\t\t<numero>" + str(aux.ObtenerNumero()) + "</numero>\n")
                archivo.write("\t\t\<titular>" + str(aux.ObtenerTitular()) + "</titular>\n")
                archivo.write("\t\t<fecha_expiracion>" + str(aux.ObtenerFecha()) + "</fecha_expiracion>\n")
                archivo.write("\t</tarjeta>\n")
                aux = aux.siguiente
            archivo.write("</tarjetas>")
            archivo.close()

    def DevolverObjetoTarjetaWeb(self,titular):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitular()==titular:
                return aux
            aux=aux.siguiente




