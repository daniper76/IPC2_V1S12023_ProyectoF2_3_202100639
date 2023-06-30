from .UsuarioActual import UsuarioActual

class LSUsuario:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def InsertarUsuario(self,usuario):
        nuevo_usuario=UsuarioActual(usuario)
        
        if self.primero == None:
            self.primero = nuevo_usuario
            self.ultimo = nuevo_usuario
        else: 
            self.ultimo.siguiente = nuevo_usuario
            self.ultimo = nuevo_usuario
    

    
    def EliminarUsuario(self,usuario):

        aux=self.primero
        anterior=None
        while aux is not None:
            if aux.ObtenerUsuario()==usuario:
                if aux==self.primero:
                    self.primero=aux.siguiente
                    aux.siguiente=None
                else:
                    anterior.siguiente=aux.siguiente
                    aux.siguiente=None
                    if(aux==self.ultimo):
                        self.ultimo=anterior
            
            anterior=aux
            aux=aux.siguiente
    
    def DevolverUsuarioActual(self):
        return self.primero.ObtenerUsuario()
    
    def ActualizarUsuario(self,usuario):
        self.primero.usuario=usuario
    