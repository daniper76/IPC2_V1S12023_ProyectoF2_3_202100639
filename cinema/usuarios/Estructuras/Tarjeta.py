class Tarjeta:
    id=1
    def __init__(self,tipo,numero,titular,fecha):
        self.tipo=tipo
        self.numero=numero
        self.titular=titular
        self.fecha=fecha
        self.id=Tarjeta.id
        Tarjeta.id+=1
        self.siguiente=None
        self.anterior=None

    def ObtenerTipo(self):
        return self.tipo
    
    def ObtenerNumero(self):
        return self.numero

    def ObtenerTitular(self):
        return self.titular
    
    def ObtenerFecha(self):
        return self.fecha
    
    def ObtenerId(self):
        return self.id