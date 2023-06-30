from .Factura import Factura

class ListaSimpleFacturas:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def InsertarFactura(self,nombre,direccion,nit,monto,cantidad_boletos,asientos,sala,pelicula,pago):
        nuevo_usuario=Factura(nombre,direccion,nit,monto,cantidad_boletos,asientos,sala,pelicula,pago)
        
        if self.primero == None:
            self.primero = nuevo_usuario
            self.ultimo = nuevo_usuario
        else: 
            self.ultimo.siguiente = nuevo_usuario
            self.ultimo = nuevo_usuario
    
    
    def loop(self):
        aux = self.primero
        while aux:
            yield aux
            aux=aux.siguiente


    def __iter__(self):
        return iter(self.loop())
    
    def DevolverObjetosFactura(self):
        aux=self.primero
        lista_facturas=[]
        while aux is not None:
            lista_facturas.append(aux)
            aux=aux.siguiente
        return lista_facturas

            

            



        

    
    




    






            

        


